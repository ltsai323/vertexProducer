import FWCore.ParameterSet.Config as cms
readFiles = cms.untracked.vstring()
readFiles.extend( [
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_325.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3250.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3251.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3252.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3253.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3254.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3255.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3256.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3257.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3258.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3259.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_326.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3260.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3261.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3262.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3263.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3264.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3265.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3266.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3267.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3268.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3269.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_327.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3270.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3271.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3272.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3273.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3274.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3275.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3276.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3277.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3278.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3279.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_328.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3280.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3281.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3282.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3283.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3284.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3285.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3286.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3287.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3288.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3289.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_329.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3290.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3291.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3292.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3293.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3294.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3295.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3296.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3297.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3298.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3299.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_33.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_330.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3300.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3301.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3302.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3303.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3304.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3305.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3306.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3307.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3308.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3309.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_331.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3310.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3311.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3312.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3313.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3314.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3315.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3316.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3317.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3318.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3319.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_332.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3320.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3321.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3322.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3323.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3324.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3325.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3326.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3327.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3328.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3329.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_333.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3330.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3331.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3332.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3333.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3334.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3335.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3336.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3337.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3338.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_3339.root"
] )
