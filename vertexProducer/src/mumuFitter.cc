// -*- C++ -*-
//
// modified from V0Fitter. It is a cmssw code used in RECO and AOD. To find Lambda0 and Kshort
// Package:    V0Producer
// Class:      V0Fitter
//
/**\class V0Fitter V0Fitter.cc RecoVertex/V0Producer/src/V0Fitter.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Brian Drell
//         Created:  Fri May 18 22:57:40 CEST 2007
// $Id: V0Fitter.cc,v 1.55 2011/11/12 01:39:27 drell Exp $
//
//

#include "vertexProducer/vertexProducer/interface/mumuFitter.h"
#include "CommonTools/CandUtils/interface/AddFourMomenta.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/PatternTools/interface/ClosestApproachInRPhi.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateTransform.h"
#include "TrackingTools/PatternTools/interface/TSCBLBuilderNoMaterial.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include <Math/Functions.h>
#include <Math/SVector.h>
#include <Math/SMatrix.h>
#include <typeinfo>
#include <memory>


// Constructor and (empty) destructor
mumuFitter::mumuFitter(const edm::ParameterSet & theParameters,
                       edm::ConsumesCollector&& iC )
{
    using std::string;
    beamspotToken = iC.consumes<reco::BeamSpot>( theParameters.getParameter<edm::InputTag>("beamspotLabel") );
    selMuonsToken = iC.consumes< myMuonList   >( theParameters.getParameter<edm::InputTag>("selMuonsLabel") );


    const std::vector < edm::ParameterSet > &pars =
        theParameters.getParameter < std::vector < edm::ParameterSet >> ("recoOptions");
    nParticles = pars.size();

    // ------> Initialize parameters from PSet. ALL TRACKED, so no defaults.
    // First set bits to do various things:
    //  -decide whether to use the KVF track smoother, and whether to store those
    //     tracks in the reco::Vertex
    useRefTrax = theParameters.getParameter < bool > (string("useSmoothing"));
    // Second, initialize post-fit cuts
    chi2Cut = theParameters.getParameter < double >(string("vtxChi2Cut"));
    rVtxCut = theParameters.getParameter < double >(string("rVtxCut"));
    tkDCACut = theParameters.getParameter < double >(string("tkDCACut"));
    vtxFitter = theParameters.getParameter < string > ("vertexFitter");
    innerHitPosCut = theParameters.getParameter < double >(string("innerHitPosCut"));

    // initialize informations for each candidates.
    optD = new double*      [nParticles];
    optB = new bool*        [nParticles];
    optS = new std::string* [nParticles];
    for (unsigned i = 0; i < nParticles; ++i)
    {
        optD[i] = new double[totNumD];
        optB[i] = new bool[totNumB];
        optS[i] = new std::string[totNumS];
    }
    // create tktk candidates lists.
    tktkCands = new reco::VertexCompositeCandidateCollection* [nParticles];
    tmpContainerToTkTkCands =  new reco::VertexCompositeCandidate* [nParticles];
    nCandsSize = new unsigned[nParticles];
    tmpContainerSize = 100;

    for (unsigned i = 0; i < nParticles; ++i)
    {
        nCandsSize[i] = 0;
        tktkCands[i] = nullptr;
        tmpContainerToTkTkCands[i] = new reco::VertexCompositeCandidate[tmpContainerSize];

        const edm::ParameterSet & subPar = pars[i];

        optS[i][candName]   = subPar.getParameter < string > (string("candName"));
        optS[i][pTkName]    = subPar.getParameter < string > (string("pTkName"));
        optS[i][nTkName]    = subPar.getParameter < string > (string("nTkName"));
        optD[i][tktkMass]   = subPar.getParameter < double > (string("tktkMass"));
        optD[i][pTkMass]    = subPar.getParameter < double > (string("pTkMass"));
        optD[i][nTkMass]    = subPar.getParameter < double > (string("nTkMass"));
        optD[i][tktkMassCut]= subPar.getParameter < double > (string("tktkMassCut"));
        optD[i][vtxSigCut]  = subPar.getParameter < double > (string("vtxSignificance2DCut"));
    }



}

mumuFitter::~mumuFitter()
{
    for (unsigned i = 0; i < nParticles; ++i)
    {
        delete[] optD[i];
        delete[] optB[i];
        delete[] optS[i];
        delete[] tmpContainerToTkTkCands[i];
        delete tktkCands[i];
    }
    delete[] optD;
    delete[] optB;
    delete[] optS;


    delete[] tmpContainerToTkTkCands;
    delete[] tktkCands;
    delete[] nCandsSize;
    return;
}

// Method containing the algorithm for vertex reconstruction
void mumuFitter::fitAll(const edm::Event & iEvent, const edm::EventSetup & iSetup)
{

    using std::vector;
    using std::cout;
    using std::endl;
    using namespace reco;
    using namespace edm;

    // Create std::vectors for Tracks and TrackRefs (required for
    //  passing to the KalmanVertexFitter)
    std::vector < TrackRef > theTrackRefs;
    std::vector < TransientTrack > theTransTracks;

    // Handles for tracks, B-field, and tracker geometry
    //Handle<reco::TrackCollection> theTrackHandle;
    Handle <   myMuonList   > theMuonsHandle;
    Handle < reco::BeamSpot > theBeamSpotHandle;



    ESHandle < MagneticField > bFieldHandle;
    ESHandle < TrackerGeometry > trackerGeomHandle;
    ESHandle < GlobalTrackingGeometry > globTkGeomHandle;

    // Get the tracks from the event, and get the B-field record
    //  from the EventSetup
   // iEvent.getByToken(selMuonsToken, theMuonsHandle);
   // iEvent.getByToken(beamspotToken, theBeamSpotHandle);
    iEvent.getByToken(selMuonsToken, theMuonsHandle);
    iEvent.getByToken(beamspotToken, theBeamSpotHandle);
    if (!theMuonsHandle->size()) return;
    if (!theBeamSpotHandle.isValid()) return;
    iSetup.get < IdealMagneticFieldRecord > ().get(bFieldHandle);
    iSetup.get < TrackerDigiGeometryRecord > ().get(trackerGeomHandle);
    iSetup.get < GlobalTrackingGeometryRecord > ().get(globTkGeomHandle);

    trackerGeom = trackerGeomHandle.product();
    magField = bFieldHandle.product();

    // Fill vectors of TransientTracks and TrackRefs after applying preselection cuts.
    theTrackRefs.reserve(theMuonsHandle->size());
    theTransTracks.reserve(theMuonsHandle->size());
    for (unsigned int indx = 0; indx < theMuonsHandle->size(); ++indx)
    {
        reco::TrackRef tmpMuonRef = theMuonsHandle->at(indx).track();
        reco::TransientTrack tmpMuonTk(*tmpMuonRef, &(*bFieldHandle), globTkGeomHandle);
        theTrackRefs.push_back(tmpMuonRef);
        theTransTracks.push_back(tmpMuonTk);
    }


    // Loop over tracks and vertex good charged track pairs
    for (unsigned int trdx1 = 0; trdx1 < theTrackRefs.size(); trdx1++)
    {

        for (unsigned int trdx2 = trdx1 + 1; trdx2 < theTrackRefs.size(); trdx2++)
        {

            //This vector holds the pair of oppositely-charged tracks to be vertexed
            std::vector < TransientTrack > transTracks;

            TrackRef positiveTrackRef;
            TrackRef negativeTrackRef;
            TransientTrack *posTransTkPtr = 0;
            TransientTrack *negTransTkPtr = 0;

            // Look at the two tracks we're looping over.  If they're oppositely
            //  charged, load them into the hypothesized positive and negative tracks
            //  and references to be sent to the KalmanVertexFitter
            if (theTrackRefs[trdx1]->charge() < 0. && theTrackRefs[trdx2]->charge() > 0.)
            {
                negativeTrackRef = theTrackRefs[trdx1];
                positiveTrackRef = theTrackRefs[trdx2];
                negTransTkPtr = &theTransTracks[trdx1];
                posTransTkPtr = &theTransTracks[trdx2];
            }
            else if (theTrackRefs[trdx1]->charge() > 0. && theTrackRefs[trdx2]->charge() < 0.)
            {
                negativeTrackRef = theTrackRefs[trdx2];
                positiveTrackRef = theTrackRefs[trdx1];
                negTransTkPtr = &theTransTracks[trdx2];
                posTransTkPtr = &theTransTracks[trdx1];
            }
            // If they're not 2 oppositely charged tracks, loop back to the
            //  beginning and try the next pair.
            else
                continue;

            // Fill the vector of TransientTracks to send to KVF
            transTracks.push_back(*posTransTkPtr);
            transTracks.push_back(*negTransTkPtr);

            // Trajectory states to calculate DCA for the 2 tracks
            FreeTrajectoryState posState = posTransTkPtr->impactPointTSCP().theState();
            FreeTrajectoryState negState = negTransTkPtr->impactPointTSCP().theState();

            if (!posTransTkPtr->impactPointTSCP().isValid() || !negTransTkPtr->impactPointTSCP().isValid())
                continue;

            // Measure distance between tracks at their closest approach
            ClosestApproachInRPhi cApp;
            cApp.calculate(posState, negState);
            if (!cApp.status())
                continue;
            float dca = fabs(cApp.distance());
            GlobalPoint cxPt = cApp.crossingPoint();

            if (dca < 0. || dca > tkDCACut)
                continue;
            if (sqrt(cxPt.x() * cxPt.x() + cxPt.y() * cxPt.y()) > 120. || std::abs(cxPt.z()) > 300.)
                continue;

            // Get trajectory states for the tracks at POCA for later cuts
            TrajectoryStateClosestToPoint posTSCP = posTransTkPtr->trajectoryStateClosestToPoint(cxPt);
            TrajectoryStateClosestToPoint negTSCP = negTransTkPtr->trajectoryStateClosestToPoint(cxPt);

            if (!posTSCP.isValid() || !negTSCP.isValid())
                continue;


            // Create the vertex fitter object and vertex the tracks
            TransientVertex theRecoVertex;
            if (vtxFitter == "KalmanVertexFitter")
            {
                KalmanVertexFitter theKalmanFitter(useRefTrax == 0 ? false : true);
                theRecoVertex = theKalmanFitter.vertex(transTracks);
            }
            else if (vtxFitter == "AdaptiveVertexFitter")
            {
                useRefTrax = false;
                AdaptiveVertexFitter theAdaptiveFitter;
                theRecoVertex = theAdaptiveFitter.vertex(transTracks);
            }
            // If the vertex is valid, make a VertexCompositeCandidate with it

            if (!theRecoVertex.isValid() || theRecoVertex.totalChiSquared() < 0.)
            {
                continue;
            }
            // Create reco::Vertex object for use in creating the Candidate
            reco::Vertex theVtx = theRecoVertex;
            // Create and fill vector of refitted TransientTracks
            //  (iff they've been created by the KVF)
            std::vector < TransientTrack > refittedTrax;
            if (theRecoVertex.hasRefittedTracks())
            {
                refittedTrax = theRecoVertex.refittedTracks();
            }
            // Do post-fit cuts if specified in config file.

            // Find the vertex d0 and its error

            typedef ROOT::Math::SMatrix < double, 3, 3, ROOT::Math::MatRepSym < double, 3 > >SMatrixSym3D;
            typedef ROOT::Math::SVector < double, 3 > SVector3;

            GlobalPoint vtxPos(theVtx.x(), theVtx.y(), theVtx.z());

            GlobalPoint beamSpotPos(theBeamSpotHandle->position().x(),
                                    theBeamSpotHandle->position().y(), theBeamSpotHandle->position().z());

            SMatrixSym3D totalCov = theBeamSpotHandle->rotatedCovariance3D() + theVtx.covariance();
            SVector3 distanceVector(vtxPos.x() - beamSpotPos.x(), vtxPos.y() - beamSpotPos.y(), 0.);    //so that we get radial values only,
            //since z beamSpot uncertainty is huge

            double rVtxMag = ROOT::Math::Mag(distanceVector);
            double sigmaRvtxMag = sqrt(ROOT::Math::Similarity(totalCov, distanceVector)) / rVtxMag;

            // The methods innerOk() and innerPosition() require TrackExtra, which
            // is only available in the RECO data tier, not AOD. Setting innerHitPosCut
            // to -1 avoids this problem and allows to run on AOD.
            if (innerHitPosCut > 0. && positiveTrackRef->innerOk())
            {
                reco::Vertex::Point posTkHitPos = positiveTrackRef->innerPosition();
                double posTkHitPosD2 =
                    (posTkHitPos.x() - beamSpotPos.x()) * (posTkHitPos.x() - beamSpotPos.x()) +
                    (posTkHitPos.y() - beamSpotPos.y()) * (posTkHitPos.y() - beamSpotPos.y());
                if (sqrt(posTkHitPosD2) < (rVtxMag - sigmaRvtxMag * innerHitPosCut)
                   )
                {
                    continue;
                }
            }
            if (innerHitPosCut > 0. && negativeTrackRef->innerOk())
            {
                reco::Vertex::Point negTkHitPos = negativeTrackRef->innerPosition();
                double negTkHitPosD2 =
                    (negTkHitPos.x() - beamSpotPos.x()) * (negTkHitPos.x() - beamSpotPos.x()) +
                    (negTkHitPos.y() - beamSpotPos.y()) * (negTkHitPos.y() - beamSpotPos.y());
                if (sqrt(negTkHitPosD2) < (rVtxMag - sigmaRvtxMag * innerHitPosCut)
                   )
                {
                    continue;
                }
            }

            if (theVtx.normalizedChi2() > chi2Cut || rVtxMag < rVtxCut )
            {
                continue;
            }
            // Cuts finished, now we create the candidates and push them back into the collections.

            std::shared_ptr < TrajectoryStateClosestToPoint > trajPlus;
            std::shared_ptr < TrajectoryStateClosestToPoint > trajMins;

            if (useRefTrax && refittedTrax.size() > 1)
            {
                // Need an iterator over the refitted tracks for below
                std::vector < TransientTrack >::iterator traxIter = refittedTrax.begin(), traxEnd = refittedTrax.end();

                // TransientTrack objects to hold the positive and negative
                //  refitted tracks
                TransientTrack *thePositiveRefTrack = 0;
                TransientTrack *theNegativeRefTrack = 0;

                for (; traxIter != traxEnd; ++traxIter)
                {
                    if (traxIter->track().charge() > 0.)
                    {
                        thePositiveRefTrack = &*traxIter;
                    }
                    else if (traxIter->track().charge() < 0.)
                    {
                        theNegativeRefTrack = &*traxIter;
                    }
                }
                if (thePositiveRefTrack == 0 || theNegativeRefTrack == 0)
                    continue;
                trajPlus.reset(new
                               TrajectoryStateClosestToPoint(thePositiveRefTrack->trajectoryStateClosestToPoint
                                       (vtxPos)));
                trajMins.reset(new
                               TrajectoryStateClosestToPoint(theNegativeRefTrack->trajectoryStateClosestToPoint
                                       (vtxPos)));
            }
            else
            {
                trajPlus.reset(new TrajectoryStateClosestToPoint(posTransTkPtr->trajectoryStateClosestToPoint(vtxPos)));
                trajMins.reset(new TrajectoryStateClosestToPoint(negTransTkPtr->trajectoryStateClosestToPoint(vtxPos)));

            }

            if (trajPlus.get() == 0 || trajMins.get() == 0 || !trajPlus->isValid() || !trajMins->isValid())
                continue;

            posTransTkPtr = negTransTkPtr = 0;

            GlobalVector positiveP(trajPlus->momentum());
            GlobalVector negativeP(trajMins->momentum());
            GlobalVector totalP(positiveP + negativeP);

            //cleanup stuff we don't need anymore
            trajPlus.reset();
            trajMins.reset();

            // start to build each tktk candidate.
            for (unsigned idx = 0; idx < nParticles; ++idx)
            {
                if (rVtxMag / sigmaRvtxMag < optD[idx][vtxSigCut]) continue;

                double pTkE = sqrt(positiveP.mag2() + optD[idx][pTkMass] * optD[idx][pTkMass]);
                double nTkE = sqrt(negativeP.mag2() + optD[idx][nTkMass] * optD[idx][nTkMass]);
                double tktkETot = pTkE + nTkE;

                using namespace reco;
                const Particle::LorentzVector tktkP4(totalP.x(), totalP.y(), totalP.z(), tktkETot);
                Particle::Point vtx(theVtx.x(), theVtx.y(), theVtx.z());
                const Vertex::CovarianceMatrix vtxCov(theVtx.covariance());
                double vtxChi2(theVtx.chi2());
                double vtxNdof(theVtx.ndof());

                reco::VertexCompositeCandidate * tktkCand =
                    new VertexCompositeCandidate(0, tktkP4, vtx, vtxCov, vtxChi2, vtxNdof);
                reco::RecoChargedCandidate pTkCand(1,
                                                   Particle::LorentzVector(positiveP.x(), positiveP.y(),
                                                           positiveP.z(), pTkE), vtx);
                pTkCand.setTrack(positiveTrackRef);
                reco::RecoChargedCandidate nTkCand(-1,
                                                   Particle::LorentzVector(negativeP.x(), negativeP.y(),
                                                           negativeP.z(), nTkE), vtx);
                nTkCand.setTrack(negativeTrackRef);
                AddFourMomenta addp4;

                tktkCand->addDaughter(pTkCand, optS[idx][pTkName]);
                tktkCand->addDaughter(nTkCand, optS[idx][nTkName]);
                tktkCand->setPdgId(0);
                addp4.set(*tktkCand);

                // fill tktkCandidates to container.
                if ( optD[idx][tktkMass] > 0. )
                {
                    if (tktkCand->mass() < optD[idx][tktkMass] + optD[idx][tktkMassCut] &&
                        tktkCand->mass() > optD[idx][tktkMass] - optD[idx][tktkMassCut])
                        tmpContainerToTkTkCands[idx][nCandsSize[idx]++] = *tktkCand;
                }
                else if (tktkCand->mass() < optD[idx][tktkMassCut] )
                    tmpContainerToTkTkCands[idx][nCandsSize[idx]++] = *tktkCand;

                // if the container spills out. create a new container.
                if ( nCandsSize[idx] == tmpContainerSize )
                    enlargeAllContainer();

                delete tktkCand;
                tktkCand = nullptr;
            } // build candidates end
        }
    } // tks loop end

    fillInContainer();
    return;
}

// Get methods
const reco::VertexCompositeCandidateCollection& mumuFitter::getCands(unsigned i) const
{
    if ( !tktkCands )
    {
        printf("tktkFitter::getCands() : no tktkCands returned, please check\n");
        exit(1);
    }
    return *(tktkCands[i]);
}

// Experimental
double mumuFitter::findV0MassError(const GlobalPoint & vtxPos,
                                   std::vector < reco::TransientTrack > dauTracks)
{
    return -1.;
}

void mumuFitter::enlargeAllContainer()
{
    reco::VertexCompositeCandidate** tmp =  new reco::VertexCompositeCandidate* [nParticles];
    // new container size;
    tmpContainerSize *= 2;

    for ( unsigned i=0; i<nParticles; ++i )
    {
        tmp[i] = new reco::VertexCompositeCandidate[tmpContainerSize];

        // copy original values to new container.
        for ( unsigned j=0; j<nCandsSize[i]; ++j )
            tmp[i][j] = tmpContainerToTkTkCands[i][j];
        // delete original container.
        delete[] tmpContainerToTkTkCands[i];
        tmpContainerToTkTkCands[i] = tmp[i];
    }
    return;
}
void mumuFitter::fillInContainer()
{
    for ( unsigned i=0; i<nParticles; ++i )
    {
        reco::VertexCompositeCandidateCollection* tmpCollection
            = new reco::VertexCompositeCandidateCollection( tmpContainerToTkTkCands[i], tmpContainerToTkTkCands[i] + nCandsSize[i]);
        tktkCands[i] = tmpCollection;
        return;
    }
}

void mumuFitter::clearSomething()
{
    for ( unsigned i=0; i<nParticles; ++i )
    {
        nCandsSize[i] = 0;
        tmpContainerSize = 100;
        delete tktkCands[i];
        delete[] tmpContainerToTkTkCands[i];

        tmpContainerToTkTkCands[i] = new reco::VertexCompositeCandidate[tmpContainerSize];
        tktkCands[i] = nullptr;
    }

}
