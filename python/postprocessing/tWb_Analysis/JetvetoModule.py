import ROOT
import numpy as np 
import sys
import os 
import json 
from correctionlib import _core
import gzip


from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module


class JetvetoModule(Module):
    def __init__(self):
        fname = "/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/2025-07-17/jetvetomaps.json.gz"
        with gzip.open(fname, "rt") as f:
            data = f.read()
            evaluator = _core.CorrectionSet.from_string(data)
        self.jetveto_map = evaluator["Summer24Prompt24_RunBCDEFGHI_V1"]


    def analyze(self,event):
        
        jets = Collection(event,"Jet")
        goodJets = []

        for jet in jets:
            veto_val = self.jetveto_map.evaluate("jetvetomap",jet.eta,jet.phi)
            if veto_val == 0:  # 0 = jet OK, !=0 = jet vetoed
                goodJets.append(jet)

        if len(goodJets) == 0:
             return False

        event.Jet = goodJets


        return True