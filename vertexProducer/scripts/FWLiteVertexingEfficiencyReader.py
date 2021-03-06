#!/usr/bin/env python
def passTrig(val, idx):
    return (abs(val)>>idx)%2
import ROOT
from DataFormats.FWLite import Events, Handle

events=Events('reco_fourTracksVertexing_9.root')
handle=Handle('int')

# don't pop up canvases
ROOT.gROOT.SetBatch()

# set white background
ROOT.gROOT.SetStyle('Plain')
label=("fourTracksFromVCCProducer:fourTracksTotallyVertexingEfficiency:myVertexingProcedure")
h_eff=ROOT.TH1I('eff','efficiency', 20, 0, 10)

for event in events:
    event.getByLabel(label,handle)
    vertexEffvalue=handle.product().get()
    print type(vertexEffvalue)
    print str(vertexEffvalue)
    print dir(vertexEffvalue)
    for idx in range(0,10):
        if passTrig(vertexEffvalue,idx):
            h_eff.Fill(idx)
        if passTrig(vertexEffvalue,0):
            h_eff.Fill(16)

#h_eff.SetMaximum(20000)
c1=ROOT.TCanvas()
h_eff.Draw()
c1.SaveAs('eff.png')

