import FWCore.ParameterSet.Config as cms


recoOptions = cms.VPSet(
        cms.PSet(
            vccLabel = cms.string('generalV0Candidates:Lambda:RECO'),
           #patLabel = cms.string('lbWriteSpecificDecay:LbTkFitted:bphAnalysis'),
            beamspotLabel = cms.string('offlineBeamSpot::RECO'),
            candName = cms.string('LambdaFromV0'),
            ),
        cms.PSet(
            vccLabel = cms.string('mumuVertexingProducer:JPsi:myVertexingProcedure'),
           #patLabel = cms.string('lbWriteSpecificDecay:LbTkFitted:bphAnalysis'),
            beamspotLabel = cms.string('offlineBeamSpot::RECO'),
            candName = cms.string('JPsiFromMuMu'),
            ),
        cms.PSet(
            vccLabel = cms.string('tktkVertexingProducer:Lam0:myVertexingProcedure'),
           #patlabel = cms.string('lbwritespecificdecay:lbtkfitted:bphanalysis'),
            beamspotLabel = cms.string('offlineBeamSpot::RECo'),
            candName = cms.string('lambdafromtktk'),
            ),
        cms.PSet(
            vccLabel = cms.string('fourTracksFromVCCProducer:LbTk:myFourTracksVertexingProcedure'),
           #patlabel = cms.string('lbwritespecificdecay:lbtkfitted:bphanalysis'),
            beamspotLabel = cms.string('offlineBeamSpot::RECO'),
            candName = cms.string('LBfromfourTracks'),
            ),
        )



