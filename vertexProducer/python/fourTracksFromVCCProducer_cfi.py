import FWCore.ParameterSet.Config as cms

fourTracksFromVCCProducer = cms.EDProducer("fourTracksFromVCCProducer",
    # set two tks information
    recoOptions = cms.VPSet(
        cms.PSet(
            # select fitting method
            fittingMethod = cms.int32(1),
            # InputTag to load from data
            tktkCandLabel = cms.InputTag('tktkVertexingProducer:TkTk:myVertexingProcedure'),
            mumuCandLabel = cms.InputTag('mumuVertexingProducer:JPsi:myVertexingProcedure'),
            beamspotLabel = cms.InputTag('offlineBeamSpot::RECO'),

            candName  = cms.string("LbTk"),
            muPosName = cms.string("MuPos"),
            muNegName = cms.string("MuNeg"),
            tkPosName = cms.string("Proton"),
            tkNegName = cms.string("Kaon"),
           #tkNegName = cms.string("Pion"),

            muPosMass = cms.double(0.1056583715),
            muNegMass = cms.double(0.1056583715),
            tkPosMass = cms.double(0.938272046),
            tkNegMass = cms.double(0.493667),
           #tkNegMass = cms.double(0.13957018),

            muPosSigma= cms.double(0.0000000035),
            muNegSigma= cms.double(0.0000000035),
            tkPosSigma= cms.double(0.000000006),
            tkNegSigma= cms.double(0.000016),
           #tkNegSigma= cms.double(0.00000035),


            # constraint used in vertexing. if -1 set. such constraint is not applied.
            mumuMassConstraint     = cms.double(3.096916),


            # selection after vertexing
            FDSigCut_mumutktkToBS  = cms.double(2.9),
            vtxprobCut             = cms.double(0.005),
            mCandMassCut           = cms.double(5.4),
            MCandMassCut           = cms.double(5.9),


            # selection before vertexing
            FDSigPreCut_tktkTomumu = cms.double(20.),
            # not used in method1
            #Cosa2dPreCut_tktkTomumu= cms.double(),

            PtPreCut_muPos         = cms.double(4.0),
            PtPreCut_muNeg         = cms.double(3.0),
            PtPreCut_tkPos         = cms.double(0.8),
            PtPreCut_tkNeg         = cms.double(0.3),

            mMassPreCut_tktk        = cms.double(-1.),
            MMassPreCut_tktk        = cms.double(2.5),
            mMassPreCut_mumu        = cms.double(3.00),
            MMassPreCut_mumu        = cms.double(3.20),
        ),
        cms.PSet(
            # select fitting method
            fittingMethod = cms.int32(2),
            # InputTag to load from data
            tktkCandLabel = cms.InputTag('tktkVertexingProducer:Lam0:myVertexingProcedure'),
            mumuCandLabel = cms.InputTag('mumuVertexingProducer:JPsi:myVertexingProcedure'),
            beamspotLabel = cms.InputTag('offlineBeamSpot::RECO'),

            candName  = cms.string("LbL0"),
            muPosName = cms.string("MuPos"),
            muNegName = cms.string("MuNeg"),
            tkPosName = cms.string("Proton"),
           #tkNegName = cms.string("Kaon"),
            tkNegName = cms.string("Pion"),

            muPosMass = cms.double(0.1056583715),
            muNegMass = cms.double(0.1056583715),
            tkPosMass = cms.double(0.938272046),
           #tkNegMass = cms.double(0.493667),
            tkNegMass = cms.double(0.13957018),

            muPosSigma= cms.double(0.0000000035),
            muNegSigma= cms.double(0.0000000035),
            tkPosSigma= cms.double(0.000000006),
           #tkNegSigma= cms.double(0.000016),
            tkNegSigma= cms.double(0.00000035),


            # constraint used in vertexing. if -1 set. such constraint is not applied.
            mumuMassConstraint     = cms.double(3.096916),



            # selection after vertexing
            FDSigCut_mumutktkToBS  = cms.double(2.9),
            vtxprobCut             = cms.double(0.005),
            mCandMassCut           = cms.double(5.4),
            MCandMassCut           = cms.double(5.9),


            # selection before vertexing
            FDSigPreCut_tktkTomumu = cms.double(5.),
            Cosa2dPreCut_tktkTomumu= cms.double(0.95),

            PtPreCut_muPos         = cms.double(4.0),
            PtPreCut_muNeg         = cms.double(3.0),
            PtPreCut_tkPos         = cms.double(0.8),
            PtPreCut_tkNeg         = cms.double(0.3),

            mMassPreCut_tktk        = cms.double(1.10),
            MMassPreCut_tktk        = cms.double(1.15),
            mMassPreCut_mumu        = cms.double(3.00),
            MMassPreCut_mumu        = cms.double(3.20),
        ),
    )
)
