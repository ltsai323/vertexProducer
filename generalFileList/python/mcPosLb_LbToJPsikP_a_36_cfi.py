import FWCore.ParameterSet.Config as cms
readFiles = cms.untracked.vstring()
readFiles.extend( [
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_641.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_642.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_643.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_644.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_645.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_646.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_647.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_648.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_649.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_65.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_650.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_651.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_652.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_653.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_654.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_655.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_656.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_657.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_658.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_659.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_66.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_660.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_661.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_662.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_663.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_664.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_665.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_666.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_667.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_668.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_669.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_67.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_670.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_671.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_672.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_673.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_674.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_675.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_676.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_677.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_678.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_679.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_68.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_680.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_681.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_682.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_683.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_684.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_685.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_686.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_687.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_688.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_689.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_69.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_690.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_691.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_692.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_693.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_694.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_695.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_696.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_697.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_698.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_699.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_7.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_70.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_700.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_701.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_702.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_703.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_704.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_705.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_706.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_707.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_708.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_709.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_71.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_710.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_711.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_712.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_713.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_714.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_715.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_716.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_717.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_718.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_719.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_72.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_720.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_721.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_722.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_723.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_724.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_725.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_726.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_727.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_728.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_729.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_73.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_730.root"
] )
