import FWCore.ParameterSet.Config as cms
readFiles = cms.untracked.vstring()
readFiles.extend( [
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_731.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_732.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_733.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_734.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_735.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_736.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_737.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_738.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_739.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_74.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_740.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_741.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_742.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_743.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_744.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_745.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_746.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_747.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_748.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_749.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_75.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_750.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_751.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_752.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_753.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_754.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_755.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_756.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_757.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_758.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_759.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_76.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_760.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_761.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_762.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_763.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_764.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_765.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_766.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_767.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_768.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_769.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_77.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_770.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_771.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_772.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_773.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_774.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_775.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_776.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_777.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_778.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_779.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_78.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_780.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_781.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_782.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_783.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_784.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_785.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_786.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_787.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_788.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_789.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_79.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_790.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_791.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_792.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_793.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_794.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_795.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_796.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_797.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_798.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_799.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_8.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_80.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_800.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_801.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_802.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_803.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_804.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_805.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_806.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_807.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_808.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_809.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_81.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_810.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_811.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_812.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_813.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_814.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_815.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_816.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_817.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_818.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_819.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_82.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_820.root"
] )
