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

#include "vertexProducer/vertexProducer/interface/ccLoader.h"
#include "CommonTools/CandUtils/interface/AddFourMomenta.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/PatternTools/interface/ClosestApproachInRPhi.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/FWLite/interface/Handle.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateTransform.h"
#include "TrackingTools/PatternTools/interface/TSCBLBuilderNoMaterial.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include <Math/Functions.h>
#include <Math/SVector.h>
#include <Math/SMatrix.h>
#include <typeinfo>
#include <memory>

#define SET_LABEL(NAME,PSET) ( NAME=PSET.getParameter<std::string>(#NAME) )
namespace
{
    const double kaonMass = 0.493667;
    const double pionMass = 0.13957018;
    const double ptonMass = 0.938272046;
    const double muonMass = 0.1056583715;
}

// Constructor and (empty) destructor
ccLoader::ccLoader(const edm::ParameterSet & theParameters,
                         edm::ConsumesCollector&& iC )
{
    using std::string;

    useVCC = (SET_LABEL(vccLabel, theParameters) != "" );
    usePAT = (SET_LABEL(patLabel, theParameters) != "" );
    useBS  = (SET_LABEL(beamspotLabel, theParameters) != "" );

    if ( useBS ) beamspotToken = iC.consumes<reco::BeamSpot>( beamspotLabel );
    if ( usePAT) patToken = iC.consumes< pat::CompositeCandidateCollection  >      ( patLabel );
    if ( useVCC) vccToken = iC.consumes< reco::VertexCompositeCandidateCollection >( vccLabel );
    if ( usePAT && useVCC )
    { printf("ccLoader : do not setup pat & vcc candidate at the same time. Check configuration files\n"); exit(1); }


    // initialize informations for each candidates.
    optD = new double[totNumD];
    optB = new bool[totNumB];
    optS = new std::string[totNumS];

    optD[mMassRegion] = theParameters.getParameter<double>("MassFrameMin");
    optD[MMassRegion] = theParameters.getParameter<double>("MassFrameMax");
    //optS[candName]   = theParameters.getParameter < string > (string("candName"));
    //optS[pTkName]    = theParameters.getParameter < string > (string("pTkName"));
    //optS[nTkName]    = theParameters.getParameter < string > (string("nTkName"));
    //optD[tktkMass]   = theParameters.getParameter < double > (string("tktkMass"));
    //optD[pTkMass]    = theParameters.getParameter < double > (string("pTkMass"));
    //optD[nTkMass]    = theParameters.getParameter < double > (string("nTkMass"));
    //optD[tktkMassCut]= theParameters.getParameter < double > (string("tktkMassCut"));
    //optD[vtxSigCut]  = theParameters.getParameter < double > (string("vtxSignificance2DCut"));


}

ccLoader::~ccLoader()
{
    delete[] optD;
    delete[] optB;
    delete[] optS;

    return;
}

// Method containing the algorithm for vertex reconstruction
void ccLoader::calc(const edm::Event & iEvent, const edm::EventSetup & iSetup)
{
    if ( !useBS )
    { printf( "beamspot label not set, please check python configuration file\n"); exit(1); }
    if ( useVCC )
    {
        edm::Handle<reco::VertexCompositeCandidateCollection> vccHandle;
        iEvent.getByToken(vccToken, vccHandle);
        reco::VertexCompositeCandidateCollection::const_iterator iter = vccHandle->cbegin();
        reco::VertexCompositeCandidateCollection::const_iterator iend = vccHandle->cend  ();
        while ( iter != iend )
        {
            const reco::VertexCompositeCandidate& cand = *iter++;
            //if ( isKshort(cand) ) continue;
            //if ( isKstar(cand) ) continue;
            //if ( isBs(cand) ) continue;
            //if ( isBd(cand) ) continue;

            fillHisto("mass", cand.mass());
        }
    }
    if ( usePAT )
    {
        edm::Handle<pat::CompositeCandidateCollection> patHandle;
        iEvent.getByToken(patToken, patHandle);
        pat::CompositeCandidateCollection::const_iterator iter = patHandle->cbegin();
        pat::CompositeCandidateCollection::const_iterator iend = patHandle->cend  ();
        while ( iter != iend )
        {
            const pat::CompositeCandidate& cand = *iter++;
            fillHisto("mass", cand.userFloat("fitMass"));
        }
    }
    return;
}

void ccLoader::setOutput( TFileDirectory* dir )
{
    _dir = dir;
    return;
}

void ccLoader::fillHisto(const std::string & name, float x)
{
    std::map < std::string, TH1 * >::iterator iter = histoMap.find(name);
    std::map < std::string, TH1 * >::iterator iend = histoMap.end();
    if (iter == iend) return;
    iter->second->Fill(x);
    return;
}
void ccLoader::createHisto(const std::string & name, int nbin, float hmin, float hmax)
{
    histoMap[name] = _dir->make < TH1F > (name.c_str(), name.c_str(), nbin, hmin, hmax);
    return;
}
void ccLoader::createHistos()
{
    createHisto("mass", 60, optD[mMassRegion], optD[MMassRegion]);

    //_dir->make<TNtupleD>("nt"
}

bool ccLoader::isKshort( reco::VertexCompositeCandidate& cand )
{
    //if ( cand.numberOfDaughters() != 2 ) return false;
    //const reco::RecoChargedCandidate* tk1Ptr = dynamic_cast<const reco::RecoChargedCandidate*>( cand.daughter(0) );
    //const reco::RecoChargedCandidate* tk2Ptr = dynamic_cast<const reco::RecoChargedCandidate*>( cand.daughter(1) );

    //TLorentzVector tk1Mom, tk2Mom;
    //tk1Mom.SetXYZM(tk1Ptr->px(), tk1Ptr->py(), tk1Ptr->pz(), pionMass);
    //tk2Mom.SetXYZM(tk2Ptr->px(), tk2Ptr->py(), tk2Ptr->pz(), pionMass);

    //if ( (tk1Mom+tk2Mom).Mag() > 0.49 &&
    //     (tk1Mom+tk2Mom).Mag() < 0.51 )  return true;
    return false;
}
bool ccLoader::isKstar( reco::VertexCompositeCandidate& cand )
{
//    if ( cand.numberOfDaughters() != 2 ) return false;
//    const reco::RecoChargedCandidate* tk1Ptr = dynamic_cast<const reco::RecoChargedCandidate*>( cand.daughter(0) );
//    const reco::RecoChargedCandidate* tk2Ptr = dynamic_cast<const reco::RecoChargedCandidate*>( cand.daughter(1) );
//
//    TLorentzVector tk1Mom, tk2Mom;
//    tk1Mom.SetXYZM(tk1Ptr->px(), tk1Ptr->py(), tk1Ptr->pz(), kaonMass);
//    tk2Mom.SetXYZM(tk2Ptr->px(), tk2Ptr->py(), tk2Ptr->pz(), pionMass);
//
//    if ( (tk1Mom+tk2Mom).Mag() > 0.8 &&
//         (tk1Mom+tk2Mom).Mag() < 1.0 )  return true;
//
//    tk1Mom.SetXYZM(tk1Ptr->px(), tk1Ptr->py(), tk1Ptr->pz(), pionMass);
//    tk2Mom.SetXYZM(tk2Ptr->px(), tk2Ptr->py(), tk2Ptr->pz(), kaonMass);
//
//    if ( (tk1Mom+tk2Mom).Mag() > 0.8 &&
//         (tk1Mom+tk2Mom).Mag() < 1.0 )  return true;
//
//
    return false;
}
bool ccLoader::isBd( reco::VertexCompositeCandidate& cand )
{
    return false;
}
bool ccLoader::isBs( reco::VertexCompositeCandidate& cand )
{
    return false;
}
