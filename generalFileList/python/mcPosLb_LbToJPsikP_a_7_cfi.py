import FWCore.ParameterSet.Config as cms
readFiles = cms.untracked.vstring()
readFiles.extend( [
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1628.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1629.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_163.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1630.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1631.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1633.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1634.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1635.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1636.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1637.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1638.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1639.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_164.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1640.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1641.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1642.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1643.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1644.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1645.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1646.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1647.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1648.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1649.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_165.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1650.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1651.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1652.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1653.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1654.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1655.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1656.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1657.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1658.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1659.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_166.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1660.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1661.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1662.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1663.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1664.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1665.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1666.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1667.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1668.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1669.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_167.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1670.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1671.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1672.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1673.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1674.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1675.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1676.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1677.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1678.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1679.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_168.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1680.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1681.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1682.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1683.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1684.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1685.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1686.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1687.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1688.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1689.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_169.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1690.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1691.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1692.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1693.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1694.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1695.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1696.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1697.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1698.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1699.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_17.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_170.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1700.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1701.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1702.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1703.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1704.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1705.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1706.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1707.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1708.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1709.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_171.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1710.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1711.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1712.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1713.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1714.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1715.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1716.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1717.root",
"file:///home/ltsai/Data/mcStep3_LbToPcK_13TeV_withoutPileUp_19426/noPreselection_vertexedpL0B/reco_myTESTfourTracksVertexingMC_1718.root"
] )