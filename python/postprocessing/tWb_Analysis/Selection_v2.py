import ROOT 
import math 
import numpy as np 
import sys 
import correctionlib
import json
import os 
from correctionlib import _core
import gzip

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.tWb_Analysis.skimtree_utils import *
#from PhysicsTools.NanoAODTools.postprocessing.Jetvetomap.Run_3_Corrections import *



class Selection_v2(Module):
    def __init__(self):
        self.writeHistFile = True

        fname = "/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/2025-07-17/jetvetomaps.json.gz"
        with gzip.open(fname, "rt") as f:
            data = f.read()
            evaluator = _core.CorrectionSet.from_string(data)
        self.jetveto_map = evaluator["Summer24Prompt24_RunBCDEFGHI_V1"]

    #Tight Lepton 
    def is_tight_muon(self,mu):
        if mu.pt < 26: return False
        if abs(mu.eta) > 2.4: return False
        if mu.pfRelIso03_all > 0.06: return False
        return True

    def is_tight_electron(self,ele):
        eta = abs(ele.eta)
        reliso = ele.pfRelIso03_all
        if ele.pt < 35: return False
        if eta > 2.1: return False 
        if 1.44 < eta < 1.57: return False
        if not ele.mvaIso_WP90: return False
        if eta < 1.44 and reliso > 0.0588: return False
        if eta >= 1.57 and reliso > 0.0571: return False
        return True
    
    
    #Loose lepton
    def is_loose_muon(self,mu):
        if mu.pt < 10: return False
        if abs(mu.eta) > 2.4: return False
        if mu.pfRelIso03_all > 0.2: return False      
        return True 


    
    def is_loose_electron(self,ele):
        if ele.pt < 15: return False
        if abs(ele.eta) > 2.5: return False
        if ele.pfRelIso03_all > 0.2: return False
        return True


    #
    def is_good_Jet(self,jet):
        if jet.pt < 40: return False
        if abs(jet.eta) > 4.7: return False
        return True        

    ##
    def is_btag(self,jet):
        if jet.pt < 40: return False
        if abs(jet.eta) > 2.4: return False
        if jet.btagUParTAK4B < 0.4648: return False
        return True




    def beginJob(self,histFile=None,histDirName=None):
        Module.beginJob(self,histFile,histDirName)
        

        #Creation of the file histo 

        #------------------------------------------------------------------------------

        #2j1b category: 

        #==================================MUON=======================================
        #
        self.h_Top_M_2j1b_Muon = ROOT.TH1F("h_Top_M_2j1b_Muon","Top mass",13,60,500)
        self.h_MtW_2j1b_Muon = ROOT.TH1F("h_MtW_2j1b_Muon","Wt mass",15,0,250)
        self.h_nEta_foward_Jet_2j1b_Muon = ROOT.TH1F("h_nEta_2j1b_Muon","Eta_foward_Jet_Muon",8,0,4.5)
        self.h_M_light_Jet_2j1b_Muon = ROOT.TH1F("h_M_light_2j1b_Muon","Mass light jet Muon ",15,0,350)
        self.h_M_b_Jet_2j1b_Muon = ROOT.TH1F("h_M_b_Jet_2j1b_Muon","Mass b jet Muon",15,0,350)
        self.h_Missing_2j1b_Muon = ROOT.TH1F("h_Missing_Energy_2j1b_Muon","Missing Trasverse Energy",15,0,200)
        self.h_Helicity_2j1b_Muon = ROOT.TH1F("h_Helicity_2j1b_Muon","Helicity angle 2j1b Muon",15,-1,1)
        self.h_Polarization_2j1b_Muon = ROOT.TH1F("h_Polarization_2j1b_Muon","Polarization angle 2j1b Muon",15,-1,1)

        
        #
        self.addObject(self.h_Top_M_2j1b_Muon)
        self.addObject(self.h_MtW_2j1b_Muon)
        self.addObject(self.h_nEta_foward_Jet_2j1b_Muon)
        self.addObject(self.h_M_light_Jet_2j1b_Muon)
        self.addObject(self.h_M_b_Jet_2j1b_Muon)
        self.addObject(self.h_Missing_2j1b_Muon)
        self.addObject(self.h_Helicity_2j1b_Muon)
        self.addObject(self.h_Polarization_2j1b_Muon)   


        #===============================ELECTRON======================================
        #
        self.h_Top_M_2j1b_Electron = ROOT.TH1F("h_Top_M_2j1b_Electron","Top mass",13,60,500) 
        self.h_MtW_2j1b_Electron = ROOT.TH1F("h_MtW_2j1b_Electron","Wt mass",15,0,250)
        self.h_nEta_foward_Jet_2j1b_Electron = ROOT.TH1F("h_nEta_2j1b_Electron","Mass_Eta_foward_Jet_Electron",8,0,4.5)
        self.h_M_light_Jet_2j1b_Electron = ROOT.TH1F("h_M_light_2j1b_Electron","Mass light jet Electron",15,0,350)
        self.h_M_b_Jet_2j1b_Electron = ROOT.TH1F("h_M_b_Jet_2j1b_Electron","Mass b jet Electron",15,0,350)
        self.h_Missing_2j1b_Electron = ROOT.TH1F("h_Missing_Energy_2j1b_Electron","Missing Trasverse Energy",15,0,200)
        self.h_Helicity_2j1b_Electron = ROOT.TH1F("h_Helicity_2j1b_Electron","Helicity angle 2j1b Electron",10,-1,1)
        self.h_Polarization_2j1b_Electron = ROOT.TH1F("h_Polarization_2j1b_Electron","Polarization angle 2j1b Electron",10,-1,1)

        ##
        self.addObject(self.h_Top_M_2j1b_Electron)
        self.addObject(self.h_MtW_2j1b_Electron)
        self.addObject(self.h_nEta_foward_Jet_2j1b_Electron)
        self.addObject(self.h_M_light_Jet_2j1b_Electron)
        self.addObject(self.h_M_b_Jet_2j1b_Electron)
        self.addObject(self.h_Missing_2j1b_Electron)
        self.addObject(self.h_Helicity_2j1b_Electron)
        self.addObject(self.h_Polarization_2j1b_Electron)
        ##

       
        #-------------------------------------------------------------------------------
       
        #3j1b
        #==================================MUON=========================================
        ##
        self.h_Top_M_bjet_3j1b_Muon = ROOT.TH1F("h_Top_M_bjet_3j1b_Muon","Top mass with bjet",13,60,500)
        self.h_Top_M_extra_3j1b_Muon = ROOT.TH1F("h_Top_M_extra_3j1b_Muon","Top mass with extra jet",13,60,500)
        self.h_MtW_3j1b_Muon = ROOT.TH1F("h_MtW_3j1b_Muon","Trasverse Mass of W",15,0,250)
        self.h_nEta_foward_Jet_3j1b_Muon = ROOT.TH1F("h_nEta_foward_Jet_3j1b_Muon","Foward Jet eTa ",8,0,4.5)
        self.h_M_b_Jet_3j1b_Muon = ROOT.TH1F("h_M_b_Jet_3j1b_Muon","Muon + bjet",15,0,350)
        self.h_M_extra_Jet_3j1b_Muon = ROOT.TH1F("h_M_extra_Jet_3j1b_Muon","Muon + extra jet",15,0,350)
        self.h_M_light_Jet_3j1b_Muon = ROOT.TH1F("h_M_light_Jet_3j1b_Muon","Muon + foward jet",15,0,350)
        self.h_Missing_3j1b_Muon = ROOT.TH1F("h_Missing_Energy_3j1b_Muon","Met Trasverse Energy",15,0,200)
        self.h_Helicity_btag_3j1b_Muon = ROOT.TH1F("h_Helicity_btag_3j1b_Muon","Helicity of the bjet",10,-1,1)
        self.h_Helicity_Extra_3j1b_Muon = ROOT.TH1F("h_Helicity_Extra_3j1b_Muon","Helicity of the extra jet",10,-1,1)
        self.h_Polarization_Extra_3j1b_Muon = ROOT.TH1F("h_Polarization_Extra_3j1b_Muon","Polarization of the Extra jet",10,-1,1)
        self.h_Polarization_btag_3j1b_Muon = ROOT.TH1F("h_Polarization_btag_3j1b_Muon","Polarization of the bjet",10,-1,1)
        self.h_Tag_score_bjet_3j1b_Muon = ROOT.TH1F("h_Tag_score_bjet_3j1b_Muon","Tag score of the Extra Jet",10,-1,1)
        ##

        ##
        self.addObject(self.h_Top_M_bjet_3j1b_Muon)
        self.addObject(self.h_Top_M_extra_3j1b_Muon)
        self.addObject(self.h_MtW_3j1b_Muon)
        self.addObject(self.h_nEta_foward_Jet_3j1b_Muon)
        self.addObject(self.h_M_b_Jet_3j1b_Muon)
        self.addObject(self.h_M_extra_Jet_3j1b_Muon)
        self.addObject(self.h_M_light_Jet_3j1b_Muon)
        self.addObject(self.h_Missing_3j1b_Muon)
        self.addObject(self.h_Helicity_btag_3j1b_Muon)   
        self.addObject(self.h_Helicity_Extra_3j1b_Muon)
        self.addObject(self.h_Polarization_btag_3j1b_Muon)
        self.addObject(self.h_Polarization_Extra_3j1b_Muon)
        self.addObject(self.h_Tag_score_bjet_3j1b_Muon)
        ##


        #==================================Electron=========================================
        ##
        self.h_Top_M_bjet_3j1b_Electron = ROOT.TH1F("h_Top_M_bjet_3j1b_Electron","Top mass with bjet",13,60,500)
        self.h_Top_M_extra_3j1b_Electron = ROOT.TH1F("h_Top_M_extra_3j1b_Electron","Top mass with extra jet",13,60,500)
        self.h_MtW_3j1b_Electron = ROOT.TH1F("h_MtW_3j1b_Electron","Trasverse Mass of W",15,0,250)
        self.h_nEta_foward_Jet_3j1b_Electron = ROOT.TH1F("h_nEta_foward_Jet_3j1b_Electron","Foward Jet eTa ",8,0,4.5)
        self.h_M_b_Jet_3j1b_Electron = ROOT.TH1F("h_M_b_Jet_3j1b_Electron","Electron + bjet",15,0,350)
        self.h_M_extra_Jet_3j1b_Electron = ROOT.TH1F("h_M_extra_Jet_3j1b_Electron","Electron + extra jet",15,0,350)
        self.h_M_light_Jet_3j1b_Electron = ROOT.TH1F("h_M_light_Jet_3j1b_Electron","Electron + foward jet",15,0,350)
        self.h_Missing_3j1b_Electron = ROOT.TH1F("h_Missing_Energy_3j1b_Electron","Met Trasverse Energy",15,0,200)
        self.h_Helicity_btag_3j1b_Electron = ROOT.TH1F("h_Helicity_btag_3j1b_Electron","Helicity of the bjet",10,-1,1)
        self.h_Helicity_Extra_3j1b_Electron = ROOT.TH1F("h_Helicity_Extra_3j1b_Electron","Helicity of the Extra jet",10,-1,1)
        self.h_Polarization_Extra_3j1b_Electron = ROOT.TH1F("h_Polarization_Extra_3j1b_Electron","Polarization of the Extra jet",10,-1,1)
        self.h_Polarization_btag_3j1b_Electron = ROOT.TH1F("h_Polarization_btag_3j1b_Electron","Polarization of the bjet",10,-1,1)
        self.h_Tag_score_bjet_3j1b_Electron = ROOT.TH1F("h_Tag_score_bjet_3j1b_Electron","Tag score of the Extra Jet",10,-1,1)
        ##

        ##
        self.addObject(self.h_Top_M_bjet_3j1b_Electron)
        self.addObject(self.h_Top_M_extra_3j1b_Electron)
        self.addObject(self.h_MtW_3j1b_Electron)
        self.addObject(self.h_nEta_foward_Jet_3j1b_Electron)
        self.addObject(self.h_M_b_Jet_3j1b_Electron)
        self.addObject(self.h_M_extra_Jet_3j1b_Electron)
        self.addObject(self.h_M_light_Jet_3j1b_Electron)
        self.addObject(self.h_Missing_3j1b_Electron)
        self.addObject(self.h_Helicity_btag_3j1b_Electron)   
        self.addObject(self.h_Helicity_Extra_3j1b_Electron)
        self.addObject(self.h_Polarization_btag_3j1b_Electron)
        self.addObject(self.h_Polarization_Extra_3j1b_Electron)
        self.addObject(self.h_Tag_score_bjet_3j1b_Electron)
        ##


        #---------------------------------------------------------------------------------------------------------------

        #3j2b
        #===================================MUON=============================================
        self.h_Top_M_3j2b_Muon = ROOT.TH1F("h_Top_M_3j2b_Muon","Top mass muon",13,60,500)
        self.h_MtW_3j2b_Muon = ROOT.TH1F("h_MtW_3j2b_Muon","Trasverse mass of W",13,0,250)
        self.h_nEta_foward_Jet_3j2b_Muon = ROOT.TH1F("h_nEta_foward_Jet_3j2b_Muon","Foward jet Eta",8,0,4.5)
        self.h_M_light_Jet_3j2b_Muon = ROOT.TH1F("h_M_light_Jet_3j2b_Muon","Muon + foward jet",15,0,350)
        self.h_M_b_Jet_3j2b_Muon = ROOT.TH1F("h_M_b_Jet_3j2b_Muon","Muon + bjet",15,0,350)
        self.h_Missing_3j2b_Muon = ROOT.TH1F("h_Missing_Energy_3j2b_Muon","Missing Trasverse Energy",15,0,200)
        self.h_Helicity_3j2b_Muon = ROOT.TH1F("h_Helicity_3j2b_Muon","Helicity angle",10,-1,1)
        self.h_Polarization_3j2b_Muon = ROOT.TH1F("h_Polarization_3j2b_Muon","Polarization angle",10,-1,1)
        self.h_Difference_eta_bjet_Muon = ROOT.TH1F("h_Difference_eta_bjet_Muon","Difference eta bjet Muon",8,0,5)


        self.addObject(self.h_Top_M_3j2b_Muon)
        self.addObject(self.h_MtW_3j2b_Muon)
        self.addObject(self.h_nEta_foward_Jet_3j2b_Muon)
        self.addObject(self.h_M_light_Jet_3j2b_Muon)
        self.addObject(self.h_M_b_Jet_3j2b_Muon)
        self.addObject(self.h_Missing_3j2b_Muon)
        self.addObject(self.h_Helicity_3j2b_Muon)
        self.addObject(self.h_Polarization_3j2b_Muon)
        self.addObject(self.h_Difference_eta_bjet_Muon)
        
        
        #===================================ELECTRON=========================================
        self.h_Top_M_3j2b_Electron = ROOT.TH1F("h_Top_M_3j2b_Electron","Top mass",13,60,500)
        self.h_MtW_3j2b_Electron = ROOT.TH1F("h_MtW_3j2b_Electron","Trasverse Mass",13,0,250)
        self.h_nEta_foward_Jet_3j2b_Electron = ROOT.TH1F("h_nEta_foward_Jet_3j2b_Electron","Eta foward jet",8,0,4.5)
        self.h_M_light_Jet_3j2b_Electron = ROOT.TH1F("h_M_light_Jet_3j2b_Electron","Electron + foward jet",15,0,350)
        self.h_M_b_Jet_3j2b_Electron = ROOT.TH1F("h_M_b_Jet_3j2b_Electron","Electron + bjet",15,0,350)
        self.h_Missing_3j2b_Electron = ROOT.TH1F("h_Missing_Energy_3j2b_Electron","Missing trasverse Energy",15,0,200)
        self.h_Helicity_3j2b_Electron = ROOT.TH1F("h_Helicity_3j2b_Electron","Helicity angle",10,-1,1)
        self.h_Polarization_3j2b_Electron = ROOT.TH1F("h_Polarization_3j2b_Electron","Polarization angle ",10,-1,1)
        self.h_Difference_eta_bjet_Electron = ROOT.TH1F("h_Difference_eta_bjet_Electron","Difference eta of bjtes Electron",8,0,5)

        #
        self.addObject(self.h_Top_M_3j2b_Electron)
        self.addObject(self.h_MtW_3j2b_Electron)
        self.addObject(self.h_nEta_foward_Jet_3j2b_Electron)
        self.addObject(self.h_M_light_Jet_3j2b_Electron)
        self.addObject(self.h_M_b_Jet_3j2b_Electron)
        self.addObject(self.h_Missing_3j2b_Electron)
        self.addObject(self.h_Helicity_3j2b_Electron)
        self.addObject(self.h_Polarization_3j2b_Electron)
        self.addObject(self.h_Difference_eta_bjet_Electron)
        

    def analyze(self,event):
        
        #Variable event histo 
        eventJet = 0
        eventLepton = 0
        LeptonCondition = False
        JetCondition = False 
        goodEvent = False
        isGoodPV = False


        #Take the Collection event and the Electron
        electrons = Collection(event,"Electron")
        muons = Collection(event,"Muon")
        jets = Collection(event,"Jet")
        MET = Object(event, "PuppiMET")
        PV = Object(event,"PV")
        HLT_muon = Object(event,"HLT_IsoMu24")
        HLT_ele = Object(event,"HLT_Ele32_eta2p1_WPTight_Gsf")

        if not HLT_muon and not HLT_ele:
            return False 


        top_nu_momentum_utils = TopUtilities()


        #Variables definite for the Analysis:
        #Top mass for category:

        Top_nu_M_2j1b_Electron = []
        Top_nu_M_2j1b_Muon = []
        Top_nu_M_btag_3j1b_Electron = []
        Top_nu_M_btag_3j1b_Muon = []
        Top_nu_M_extra_3j1b_Electron = []
        Top_nu_M_extra_3j1b_Muon = []
        Top_nu_M_3j2b_Electron = [] 
        Top_nu_M_3j2b_Muon = []


        #Trasverse mass of W:
        MtW_2j1b_Muon = []        
        MtW_2j1b_Electron = []

        MtW_3j1b_Muon = []
        MtW_3j1b_Electron = []

        MtW_3j2b_Muon = []
        MtW_3j2b_Electron = []


        #Foward Jet eta:

        nEta_foward_Jet_2j1b_Electron = [] 
        nEta_foward_Jet_2j1b_Muon = []

        nEta_foward_Jet_3j1b_Electron = []
        nEta_foward_Jet_3j1b_Muon = []

        nEta_foward_Jet_3j2b_Electron = []
        nEta_foward_Jet_3j2b_Muon = []


        #Mass lepton + foward jet

        M_light_Jet_2j1b_Electron = []
        M_light_Jet_2j1b_Muon = []

        M_light_Jet_3j1b_Electron = []
        M_light_Jet_3j1b_Muon = []

        M_light_Jet_3j2b_Electron = []
        M_light_Jet_3j2b_Muon = []
 
        #Mass lepton + extra jet

        M_Extra_Jet_3j1b_Electron = []
        M_Extra_Jet_3j1b_Muon = []

        #Mass lepton + bjet tag: 

        M_b_Jet_2j1b_Electron = []
        M_b_Jet_2j1b_Muon = []

        M_b_Jet_3j1b_Electron = []
        M_b_Jet_3j1b_Muon = []


        M_b_Jet_3j2b_Electron = []
        M_b_Jet_3j2b_Muon = []


        #Missing_Energy:
        Missing_trasverse_Energy_2j1b_Electron = []
        Missing_trasverse_Energy_2j1b_Muon = []

        Missing_trasverse_Energy_3j1b_Electron = []
        Missing_trasverse_Energy_3j1b_Muon = []


        Missing_trasverse_Energy_3j2b_Electron = []
        Missing_trasverse_Energy_3j2b_Muon = []


        #Helicity angle 
        Helicity_angle_2j1b_Electron = []
        Helicity_angle_2j1b_Muon = []

        Helicity_angle_btag_3j1b_Electron = []
        Helicity_angle_btag_3j1b_Muon = []

        Helicity_angle_Extra_3j1b_Electron = []
        Helicity_angle_Extra_3j1b_Muon = []


        Helicity_angle_3j2b_Electron = []
        Helicity_angle_3j2b_Muon = []


        #Polarization angle 

        Polarization_angle_2j1b_Electron = []
        Polarization_angle_2j1b_Muon = []


        Polarization_angle_btag_3j1b_Electron = []
        Polarization_angle_btag_3j1b_Muon = []


        Polarization_angle_Extra_3j1b_Electron = []
        Polarization_angle_Extra_3j1b_Muon = []


        Polarization_angle_3j2b_Electron = []
        Polarization_angle_3j2b_Muon = []

        #Tag score extra jet 
        Tag_score_btag_Electron = []
        Tag_score_btag_Muon = []

        #Difference eta bjet 
        Difference_eta_bjet_Electron = []
        Difference_eta_bjet_Muon = []



        #See if the Particle Vertex is Ok
        isGoodPV = (PV.ndof > 4 and abs(PV.z) < 20 and math.hypot(PV.x,PV.y)<2) 


        #Tight Selection of Leptons
        goodMu = list(filter(self.is_tight_muon,muons))
        goodEle = list(filter(self.is_tight_electron,electrons))
        looseMu = [m for m in muons if self.is_loose_muon(m) and m not in goodMu]
        looseEle = [e for e in electrons if self.is_loose_electron(e) and e not in goodEle]





        #Selection of Jets
        #goodJets =list(filter(self.is_good_Jet,jets)) 

        goodJets_veto = []
        
        for jet in jets:
            veto_val = self.jetveto_map.evaluate("jetvetomap", jet.eta, jet.phi)
            if veto_val == 0:  # 0 = ok, !=0 = vetoed
                goodJets_veto.append(jet)




        goodJets = list(filter(self.is_good_Jet,goodJets_veto))
        bJets = list(filter(self.is_btag,goodJets))

 
 
        #Number of the different Collection 
        nJets  = len(goodJets)
        nBjets = len(bJets)
        
        #Number of tight leptons
        nGoodMu = len(goodMu)
        nGoodEle = len(goodEle)
        
        #Number of loose leptons
        nLooseMu = len(looseMu)
        nLooseEle = len(looseEle)

        #Jet condition  
        JetCondition = ((nJets == 2 and nBjets == 1) or (nJets == 3 and (nBjets == 1 or nBjets == 2)))


        if (nGoodMu == 1 and nGoodEle == 0 and nLooseMu == 0 and nLooseEle == 0):
            #
            LeptonCondition = True
            eventLepton = 1
            #
            tightLepton = goodMu[0]
            for j in goodJets:
                dR = deltaR(j.eta, j.phi, tightLepton.eta, tightLepton.phi)
                if dR < 0.4:
                    return False
        

        if (nGoodEle == 1 and nGoodMu == 0 and nLooseEle == 0 and nLooseMu == 0):
            #
            LeptonCondition = True
            eventLepton = 2
            #
            tightLepton = goodEle[0]
            for j in goodJets:
                dR = deltaR(j.eta, j.phi, tightLepton.eta, tightLepton.phi)
                if dR < 0.4:
                    return False


        goodEvent = LeptonCondition and JetCondition and isGoodPV

        if goodEvent:
            if nJets == 2 and nBjets == 1:
                eventJet = 1
            elif nJets == 3 and nBjets == 1:
                eventJet = 2
            elif nJets == 3 and nBjets == 2:
                eventJet = 3
        else: 
            return False



        #Define a TLorentz vector for the top candidate
        top_nu_momentum = ROOT.TLorentzVector()
        
        #===============================================
        #===============MUON EVENT======================
        #===============================================
        

        #===================2j1b========================
        if eventLepton == 1 and eventJet == 1: 
            mu = goodMu[0]

            #Identify the non b jet in the files:
            non_b_jets = [j for j in goodJets if j not in bJets]
            
            if len(non_b_jets) != 1:
                return False
            
            nEta_foward_Jet_2j1b_Muon.append(abs(non_b_jets[0].eta))

            for b in bJets:
                top_nu_momentum, IsmcNeg, mcdR_lepjet, neutrino = top_nu_momentum_utils.topnu_4Momentum(
                    lepton=mu.p4(),
                    jet=b.p4(),
                    metPx=MET.pt * math.cos(MET.phi),
                    metPy=MET.pt * math.sin(MET.phi)
                )

                if top_nu_momentum:
                    #Mass of top recostructed 
                    Top_nu_M_2j1b_Muon.append(top_nu_momentum.M())
                                        

                    #Helicity angle and Polarization angle
                    W = mu.p4()+neutrino
                    
                    #W boost
                    boost_top = -top_nu_momentum.BoostVector()
                    W_in_top = ROOT.TLorentzVector(W)
                    W_in_top.Boost(boost_top)
                    W_dir_top = W_in_top.Vect().Unit()

                    #Lepton boost 
                    boost_W = -W.BoostVector()
                    lep_in_W = ROOT.TLorentzVector(mu.p4())
                    lep_in_top = ROOT.TLorentzVector(mu.p4())
                    lep_in_W.Boost(boost_W)
                    lep_in_top.Boost(boost_top)
                    lep_dir_W = lep_in_W.Vect().Unit()
                    lep_dir_top = lep_in_top.Vect().Unit()


                    costheta_star = W_dir_top.Dot(lep_dir_W)
                    cospol_star = W_dir_top.Dot(lep_dir_top)

                    if (costheta_star < 1 and costheta_star > -1):
                        Helicity_angle_2j1b_Muon.append(costheta_star)
                    if (cospol_star < 1 and cospol_star > -1):    
                        Polarization_angle_2j1b_Muon.append(cospol_star)


                #Muon + the bjet:
                lep_bjet_p4 = mu.p4()+b.p4()
                M_lbj = lep_bjet_p4.M()
                M_b_Jet_2j1b_Muon.append(M_lbj)


            #Trasverse Mass of W:
            lepton_p4 = mu.p4
            delta_phi = mu.phi - MET.phi
            m_TW = math.sqrt(2 * mu.pt * MET.pt * (1 - math.cos(delta_phi)))

            #Missing trasverse Energy:
            Missing_trasverse_Energy_2j1b_Muon.append(MET.pt)


            if m_TW: 
                MtW_2j1b_Muon.append(m_TW)

            #Muon+Foward Jet:
            lep_Fjet_p4 = mu.p4()+non_b_jets[0].p4()
            M_lFj = lep_Fjet_p4.M()
            M_light_Jet_2j1b_Muon.append(M_lFj)

        #===============3j1b=========================
        if eventLepton == 1 and eventJet == 2: 
            mu = goodMu[0]

            non_b_jets = [j for j in goodJets if j not in bJets]
            if len(non_b_jets) != 2:
                return False  # skipa l'evento se ci sono più di 2b_jet in questa categoria.

            # seleziona quello con |η| minore
            jet_selected = min(non_b_jets, key=lambda x: abs(x.eta))
            # selezione quello con |η| max
            foward_jet = max(non_b_jets, key = lambda x: abs(x.eta))

            #Eta of the foward jet             
            nEta_foward_Jet_3j1b_Muon.append(abs(foward_jet.eta))
            #Tag score of the extra jet not b-tagged
            Tag_score_btag_Muon.append(jet_selected.btagUParTAK4B)

            #Cycle on the bjtes:
            for b in bJets:
                
                
                top_nu_momentum, IsmcNeg, mcdR_lepjet, neutrino = top_nu_momentum_utils.topnu_4Momentum(
                    lepton=mu.p4(),
                    jet=b.p4(),
                    metPx=MET.pt * math.cos(MET.phi),
                    metPy=MET.pt * math.sin(MET.phi)
                )
                
                
                
                if top_nu_momentum:
                    Top_nu_M_btag_3j1b_Muon.append(top_nu_momentum.M())
                    
                    #Helicity angle 
                    W = mu.p4()+neutrino
                    
                    #W boost
                    boost_top = -top_nu_momentum.BoostVector()
                    W_in_top = ROOT.TLorentzVector(W)
                    W_in_top.Boost(boost_top)
                    W_dir_top = W_in_top.Vect().Unit()

                    #Lepton boost 
                    boost_W = -W.BoostVector()
                    lep_in_W = ROOT.TLorentzVector(mu.p4())
                    lep_in_top = ROOT.TLorentzVector(mu.p4())
                    lep_in_W.Boost(boost_W)
                    lep_in_top.Boost(boost_top)
                    lep_dir_W = lep_in_W.Vect().Unit()
                    lep_dir_top = lep_in_top.Vect().Unit()

                    costheta_star = W_dir_top.Dot(lep_dir_W)
                    cospol_star = W_dir_top.Dot(lep_dir_top)


                    if (costheta_star <= 1 and costheta_star >= -1) :
                        Helicity_angle_btag_3j1b_Muon.append(costheta_star)
                        
                    if (cospol_star < 1 and cospol_star > -1):
                        Polarization_angle_btag_3j1b_Muon.append(cospol_star)

                #Muon+bJet:
                lep_bjet_p4 = mu.p4()+b.p4()
                M_lbj = lep_bjet_p4.M()
                M_b_Jet_3j1b_Muon.append(M_lbj)

            
            
            # ricostruisci il top anche usando il jet secondario (non b-tagged)
            top_nu_momentum, IsmcNeg, mcdR_lepjet, neutrino = top_nu_momentum_utils.topnu_4Momentum(
            lepton=mu.p4(),
            jet=jet_selected.p4(),
            metPx=MET.pt * math.cos(MET.phi),
            metPy=MET.pt * math.sin(MET.phi)
            )
            if top_nu_momentum:
                Top_nu_M_extra_3j1b_Muon.append(top_nu_momentum.M())

                #Helicity angle 
                W = mu.p4()+neutrino
                
                #W boost
                boost_top = -top_nu_momentum.BoostVector()
                W_in_top = ROOT.TLorentzVector(W)
                W_in_top.Boost(boost_top)
                W_dir_top = W_in_top.Vect().Unit()

                #Lepton boost 
                boost_W = -W.BoostVector()
                lep_in_W = ROOT.TLorentzVector(mu.p4())
                lep_in_top = ROOT.TLorentzVector(mu.p4())
                lep_in_W.Boost(boost_W)
                lep_in_top.Boost(boost_top)
                lep_dir_W = lep_in_W.Vect().Unit()
                lep_dir_top = lep_in_top.Vect().Unit()

                costheta_star = W_dir_top.Dot(lep_dir_W)
                cospol_star = W_dir_top.Dot(lep_dir_top)

                if (costheta_star <= 1 and costheta_star >= -1): 
                    Helicity_angle_Extra_3j1b_Muon.append(costheta_star)
                if (cospol_star >= -1 and cospol_star <= 1):    
                    Polarization_angle_Extra_3j1b_Muon.append(cospol_star)



            #Calcolo massa Trasversa W
            lepton_p4 = mu.p4

            # Componenti neutrino approsimato MET 

            pt_nu = MET.pt 
            px_nu = MET.pt * math.cos(MET.phi)
            py_nu = MET.pt * math.sin(MET.phi)

            
            # Componenti del leptone
            pt_l = mu.pt
            px_l = mu.pt*math.cos(mu.phi)
            py_l = mu.pt*math.sin(mu.phi)


             
            # Formula m_TW
            #m_TW = math.sqrt((pt_l + pt_nu)**2 - (px_l + px_nu)**2 - (py_l + py_nu)**2)
            delta_phi = mu.phi - MET.phi
            m_TW = math.sqrt(2 * mu.pt * MET.pt * (1 - math.cos(delta_phi)))



            if m_TW: 
                MtW_3j1b_Muon.append(m_TW)


            #Muon+extra_Jet:
            lep_Ejet_p4 = mu.p4()+jet_selected.p4()
            M_lEj = lep_Ejet_p4.M()
            M_Extra_Jet_3j1b_Muon.append(M_lEj)

            #Muon+Foward_Jet:
            lep_Fjet_p4 = mu.p4()+foward_jet.p4()
            M_lFj = lep_Fjet_p4.M()
            M_light_Jet_3j1b_Muon.append(M_lFj)
       
            #Missing trasverse Energy
            Missing_trasverse_Energy_3j1b_Muon.append(MET.pt)



        #3j2b 
        if (eventLepton == 1) and (eventJet == 3): 
            mu = goodMu[0]

            non_b_jets = [j for j in goodJets if j not in bJets]
            
            if len(non_b_jets)!=1: 
                return False
            
            nEta_foward_Jet_3j2b_Muon.append(abs(non_b_jets[0].eta))

            #Difference eta of the two bjet 
            if len(bJets) == 2:
                deltaEta_b = abs(bJets[0].eta-bJets[1].eta)
                Difference_eta_bjet_Muon.append(deltaEta_b)

            for b in bJets:
                
                top_nu_momentum, IsmcNeg, mcdR_lepjet, neutrino = top_nu_momentum_utils.topnu_4Momentum(
                    lepton=mu.p4(),
                    jet=b.p4(),
                    metPx=MET.pt * math.cos(MET.phi),
                    metPy=MET.pt * math.sin(MET.phi)
                )
                
                if top_nu_momentum:
                    Top_nu_M_3j2b_Muon.append(top_nu_momentum.M())

                    #Helicity angle 
                    W = mu.p4()+neutrino
                    
                    #W boost
                    boost_top = -top_nu_momentum.BoostVector()
                    W_in_top = ROOT.TLorentzVector(W)
                    W_in_top.Boost(boost_top)
                    W_dir_top = W_in_top.Vect().Unit()

                    #Lepton boost 
                    boost_W = -W.BoostVector()
                    lep_in_W = ROOT.TLorentzVector(mu.p4())
                    lep_in_top = ROOT.TLorentzVector(mu.p4())
                    lep_in_W.Boost(boost_W)
                    lep_in_top.Boost(boost_top)
                    lep_dir_W = lep_in_W.Vect().Unit()
                    lep_dir_top = lep_in_top.Vect().Unit()

                    costheta_star = W_dir_top.Dot(lep_dir_W)
                    cospol_star = W_dir_top.Dot(lep_dir_top)

                    if costheta_star < 1 and costheta_star > -1:
                        Helicity_angle_3j2b_Muon.append(costheta_star)
                    if cospol_star < 1 and cospol_star > -1:
                        Polarization_angle_3j2b_Muon.append(cospol_star)
                    

                #Muon + b jet:
                lep_bjet_p4 = mu.p4()+b.p4()
                M_lbj = lep_bjet_p4.M()
                M_b_Jet_3j2b_Muon.append(M_lbj)

            #Calcolo massa Trasversa W
            lepton_p4 = mu.p4

            # Componenti neutrino approsimato MET 

            pt_nu = MET.pt 
            px_nu = MET.pt * math.cos(MET.phi)
            py_nu = MET.pt * math.sin(MET.phi)


            # Componenti del leptone
            pt_l = mu.pt
            px_l = mu.pt*math.cos(mu.phi)
            py_l = mu.pt*math.sin(mu.phi)


             
            # Formula m_TW
            #m_TW = math.sqrt((pt_l + pt_nu)**2 - (px_l + px_nu)**2 - (py_l + py_nu)**2)
            delta_phi = mu.phi - MET.phi
            m_TW = math.sqrt(2 * mu.pt * MET.pt * (1 - math.cos(delta_phi)))


            if m_TW: 
                MtW_3j2b_Muon.append(m_TW)

            #Muon + light jet:
            lep_Fjet_p4 = mu.p4()+non_b_jets[0].p4()       
            M_lFj = lep_Fjet_p4.M()
            M_light_Jet_3j2b_Muon.append(M_lFj)
       
            #Missing trasverse Energy
            Missing_trasverse_Energy_3j2b_Muon.append(MET.pt)


        #=========================================================
        #====================ELECTRON=============================
        #=========================================================

        #2j1b event 

        if (eventLepton == 2) and (eventJet == 1):
            
            ele = goodEle[0]

            # Take the not bjet 
            non_b_jets = [j for j in goodJets if j not in bJets]
            
            if len(non_b_jets) != 1:
                return False
            
            nEta_foward_Jet_2j1b_Electron.append(abs(non_b_jets[0].eta))

            #Ricostruzione top con i bjet taggati
            for b in bJets:
                #b = jets[b_idx]
                
                top_nu_momentum, IsmcNeg, mcdR_lepjet, neutrino = top_nu_momentum_utils.topnu_4Momentum(
                    lepton=ele.p4(),
                    jet=b.p4(),
                    metPx=MET.pt * math.cos(MET.phi),
                    metPy=MET.pt * math.sin(MET.phi)
                )
                
                
                if top_nu_momentum:
            
                    Top_nu_M_2j1b_Electron.append(top_nu_momentum.M())
                
                    #Helicity angle 
                    W = ele.p4()+neutrino
                    
                    #W boost
                    boost_top = -top_nu_momentum.BoostVector()
                    W_in_top = ROOT.TLorentzVector(W)
                    W_in_top.Boost(boost_top)
                    W_dir_top = W_in_top.Vect().Unit()

                    #Lepton boost 
                    boost_W = -W.BoostVector()
                    lep_in_W = ROOT.TLorentzVector(ele.p4())
                    lep_in_top = ROOT.TLorentzVector(ele.p4())
                    lep_in_W.Boost(boost_W)
                    lep_in_top.Boost(boost_top)
                    lep_dir_W = lep_in_W.Vect().Unit()
                    lep_dir_top = lep_in_top.Vect().Unit()

                    costheta_star = W_dir_top.Dot(lep_dir_W)
                    cospol_star = W_dir_top.Dot(lep_dir_top)

                    if costheta_star < 1 and costheta_star > -1:
                        Helicity_angle_2j1b_Electron.append(costheta_star)
                    if cospol_star < 1 and cospol_star > -1:
                        Polarization_angle_2j1b_Electron.append(cospol_star)

                #Electron+bJet
                lep_bjet_p4 = ele.p4()+b.p4()
                M_lbj = lep_bjet_p4.M()    
                M_b_Jet_2j1b_Electron.append(M_lbj)

            #Calcolo massa Trasversa W
            lepton_p4 = ele.p4

            # Componenti neutrino approsimato MET 

            pt_nu = MET.pt 
            px_nu = MET.pt * math.cos(MET.phi)
            py_nu = MET.pt * math.sin(MET.phi)

            # Componenti del leptone
            pt_l = ele.pt
            px_l = ele.pt*math.cos(ele.phi)
            py_l = ele.pt*math.sin(ele.phi)

             
            # Formula m_TW
            #m_TW = math.sqrt((pt_l + pt_nu)**2 - (px_l + px_nu)**2 - (py_l + py_nu)**2)
            delta_phi = ele.phi - MET.phi
            m_TW = math.sqrt(2 * ele.pt * MET.pt * (1 - math.cos(delta_phi)))


            if m_TW: 
                MtW_2j1b_Electron.append(m_TW)
            
            #Electron + Foward jet:
            lep_Fjet_p4 = ele.p4()+non_b_jets[0].p4()
            M_lFj = lep_Fjet_p4.M()
            M_light_Jet_2j1b_Electron.append(M_lFj)        
            
            #Missing trasverse Energy:
            Missing_trasverse_Energy_2j1b_Electron.append(MET.pt)


        #3j1b: Electron event 

        if (eventLepton == 2) and (eventJet == 2):
            ele = goodEle[0]

            # identifica i non-b-jet
            non_b_jets = [j for j in goodJets if j not in bJets]
            if len(non_b_jets) != 2:
                return False  # skipa l'evento se ci sono più di 2b_jet in questa categoria.

            # seleziona quello con |η| minore
            jet_selected = min(non_b_jets, key=lambda x: abs(x.eta))
            # selezione quello con |η| max
            foward_jet = max(non_b_jets, key = lambda x: abs(x.eta))

            nEta_foward_Jet_3j1b_Electron.append(abs(foward_jet.eta))
            
            Tag_score_btag_Electron.append(jet_selected.btagUParTAK4B)


            for b in bJets:
                #
                top_nu_momentum, IsmcNeg, mcdR_lepjet, neutrino = top_nu_momentum_utils.topnu_4Momentum(
                    lepton=ele.p4(),
                    jet=b.p4(),
                    metPx=MET.pt * math.cos(MET.phi),
                    metPy=MET.pt * math.sin(MET.phi)
                )
                
                
                if top_nu_momentum:
                    Top_nu_M_btag_3j1b_Electron.append(top_nu_momentum.M())
                    
                    #Helicity angle 
                    W = ele.p4()+neutrino
                    
                    #W boost
                    boost_top = -top_nu_momentum.BoostVector()
                    W_in_top = ROOT.TLorentzVector(W)
                    W_in_top.Boost(boost_top)
                    W_dir_top = W_in_top.Vect().Unit()

                    #Lepton boost 
                    boost_W = -W.BoostVector()
                    lep_in_W = ROOT.TLorentzVector(ele.p4())
                    lep_in_top = ROOT.TLorentzVector(ele.p4())
                    lep_in_W.Boost(boost_W)
                    lep_in_top.Boost(boost_top)
                    lep_dir_W = lep_in_W.Vect().Unit()
                    lep_dir_top = lep_in_top.Vect().Unit()

                    costheta_star = W_dir_top.Dot(lep_dir_W)
                    cospol_star = W_dir_top.Dot(lep_dir_top)


                    if costheta_star <= 1 and costheta_star >= -1:
                        Helicity_angle_btag_3j1b_Electron.append(costheta_star)
                    if cospol_star <= 1 and cospol_star >= -1:
                        Polarization_angle_btag_3j1b_Electron.append(cospol_star)
                
                ##
                lep_bjet_p4 = ele.p4()+b.p4()
                M_lbj = lep_bjet_p4.M()
                M_b_Jet_3j1b_Electron.append(M_lbj)
                ##

            # ricostruisci il top anche usando il jet secondario (non b-tagged)
            top_nu_momentum, IsmcNeg, mcdR_lepjet, neutrino = top_nu_momentum_utils.topnu_4Momentum(
            lepton=ele.p4(),
            jet=jet_selected.p4(),
            metPx=MET.pt * math.cos(MET.phi),
            metPy=MET.pt * math.sin(MET.phi)
            )
            
            if top_nu_momentum:
                Top_nu_M_extra_3j1b_Electron.append(top_nu_momentum.M())

                #Helicity angle 
                W = ele.p4()+neutrino
                
                #W boost
                boost_top = -top_nu_momentum.BoostVector()
                W_in_top = ROOT.TLorentzVector(W)
                W_in_top.Boost(boost_top)
                W_dir_top = W_in_top.Vect().Unit()

                #Lepton boost 
                boost_W = -W.BoostVector()
                lep_in_W = ROOT.TLorentzVector(ele.p4())
                lep_in_top = ROOT.TLorentzVector(ele.p4())
                lep_in_W.Boost(boost_W)
                lep_in_top.Boost(boost_top)
                lep_dir_W = lep_in_W.Vect().Unit()
                lep_dir_top = lep_in_top.Vect().Unit()

                costheta_star = W_dir_top.Dot(lep_dir_W)
                cospol_star = W_dir_top.Dot(lep_dir_top)

                if costheta_star <= 1 and costheta_star >= -1: 
                    Helicity_angle_Extra_3j1b_Electron.append(costheta_star)
                if cospol_star <= 1 and cospol_star >= -1: 
                    Polarization_angle_Extra_3j1b_Electron.append(cospol_star)



            #Calcolo massa Trasversa W
            lepton_p4 = ele.p4()

            # Componenti neutrino approsimato MET 

            pt_nu = MET.pt 
            px_nu = MET.pt * math.cos(MET.phi)
            py_nu = MET.pt * math.sin(MET.phi)


            # Componenti del leptone
            pt_l = ele.pt
            px_l = ele.pt*math.cos(ele.phi)
            py_l = ele.pt*math.sin(ele.phi)


             
            # Formula m_TW
            #m_TW = math.sqrt((pt_l + pt_nu)**2 - (px_l + px_nu)**2 - (py_l + py_nu)**2)
            delta_phi = ele.phi - MET.phi
            m_TW = math.sqrt(2 * ele.pt * MET.pt * (1 - math.cos(delta_phi)))



            if m_TW: 
                MtW_3j1b_Electron.append(m_TW)


            #Muon+extra_Jet:
            lep_Ejet_p4 = ele.p4()+jet_selected.p4()
            M_lEj = lep_Ejet_p4.M()
            M_Extra_Jet_3j1b_Electron.append(M_lEj)

            #Muon+Foward_Jet:
            lep_Fjet_p4 = ele.p4()+foward_jet.p4()
            M_lFj = lep_Fjet_p4.M()
            M_light_Jet_3j1b_Electron.append(M_lFj)


            #Missing trasverse Energy:
            Missing_trasverse_Energy_3j1b_Electron.append(MET.pt)

        #3j2b Electron 
        if (eventLepton == 2) and (eventJet == 3):
            ele = goodEle[0]

            non_b_jets = [j for j in goodJets if j not in bJets]
            
            if len(non_b_jets)!=1: 
                return False
            
            nEta_foward_Jet_3j2b_Electron.append(abs(non_b_jets[0].eta))
            

            #Difference eta of the two bjet 
            if len(bJets) == 2:
                deltaEta_b = abs(bJets[0].eta-bJets[1].eta)
                Difference_eta_bjet_Electron.append(deltaEta_b)

            
            for b in bJets:

                top_nu_momentum, IsmcNeg, mcdR_lepjet, neutrino = top_nu_momentum_utils.topnu_4Momentum(
                    lepton=ele.p4(),
                    jet=b.p4(),
                    metPx=MET.pt * math.cos(MET.phi),
                    metPy=MET.pt * math.sin(MET.phi)
                )
                if top_nu_momentum:
                    Top_nu_M_3j2b_Electron.append(top_nu_momentum.M())

                    #Helicity angle 
                    W = ele.p4()+neutrino
                    
                    #W boost
                    boost_top = -top_nu_momentum.BoostVector()
                    W_in_top = ROOT.TLorentzVector(W)
                    W_in_top.Boost(boost_top)
                    W_dir_top = W_in_top.Vect().Unit()

                    #Lepton boost 
                    boost_W = -W.BoostVector()
                    lep_in_W = ROOT.TLorentzVector(ele.p4())
                    lep_in_top = ROOT.TLorentzVector(ele.p4())
                    lep_in_W.Boost(boost_W)
                    lep_in_top.Boost(boost_top)
                    lep_dir_W = lep_in_W.Vect().Unit()
                    lep_dir_top = lep_in_top.Vect().Unit()

                    costheta_star = W_dir_top.Dot(lep_dir_W)
                    cospol_star = W_dir_top.Dot(lep_dir_top)



                    if costheta_star < 1 and costheta_star > -1:
                        Helicity_angle_3j2b_Electron.append(costheta_star)
                    if cospol_star < 1 and cospol_star > -1:
                        Polarization_angle_3j2b_Electron.append(cospol_star)

                #Electron + b jet:
                lep_bjet_p4 = ele.p4()+b.p4()
                M_lbj = lep_bjet_p4.M()
                M_b_Jet_3j2b_Electron.append(M_lbj)

                

            #Calcolo massa Trasversa W
            lepton_p4 = ele.p4

            # Componenti neutrino approsimato MET 

            pt_nu = MET.pt 
            px_nu = MET.pt * math.cos(MET.phi)
            py_nu = MET.pt * math.sin(MET.phi)


            #Componenti del leptone
            pt_l = ele.pt
            px_l = ele.pt*math.cos(ele.phi)
            py_l = ele.pt*math.sin(ele.phi)


             
            # Formula m_TW
            #m_TW = math.sqrt((pt_l + pt_nu)**2 - (px_l + px_nu)**2 - (py_l + py_nu)**2)
            delta_phi = ele.phi - MET.phi
            m_TW = math.sqrt(2 * ele.pt * MET.pt * (1 - math.cos(delta_phi)))



            if m_TW: 
                MtW_3j2b_Electron.append(m_TW)
            

            #Missing trasverse Energy
            Missing_trasverse_Energy_3j2b_Electron.append(MET.pt)
            
            #Muon + light jet:
            lep_Fjet_p4 = ele.p4()+non_b_jets[0].p4()       
            M_lFj = lep_Fjet_p4.M()
            M_light_Jet_3j2b_Electron.append(M_lFj)




        #FILL THE HISTO 
        #######################################################
        ####################MUON EVENT#########################
        #######################################################
        
        
        #2j1b event  
        for Transfer in Top_nu_M_2j1b_Muon:
            self.h_Top_M_2j1b_Muon.Fill(Transfer)
        for Transfer in MtW_2j1b_Muon:
            self.h_MtW_2j1b_Muon.Fill(Transfer)
        for Transfer in nEta_foward_Jet_2j1b_Muon:
            self.h_nEta_2j1b_Muon.Fill(Transfer)
        for Transfer in M_light_Jet_2j1b_Muon:
            self.h_M_light_Jet_2j1b_Muon.Fill(Transfer)
        for Transfer in M_b_Jet_2j1b_Muon:
            self.h_M_b_Jet_2j1b_Muon.Fill(Transfer)
        for Transfer in Missing_trasverse_Energy_2j1b_Muon:
            self.h_Missing_2j1b_Muon.Fill(Transfer)
        for Transfer in Helicity_angle_2j1b_Muon:
            self.h_Helicity_2j1b_Muon.Fill(Transfer)
        for Transfer in Polarization_angle_2j1b_Muon:
            self.h_Polarization_2j1b_Muon.Fill(Transfer)
    
        #3j1b event 

        for Transfer in Top_nu_M_btag_3j1b_Muon:
            self.h_Top_M_bjet_3j1b_Muon.Fill(Transfer)
        for Transfer in Top_nu_M_extra_3j1b_Muon:
            self.h_Top_M_extra_3j1b_Muon.Fill(Transfer)
        for Transfer in MtW_3j1b_Muon:
            self.h_MtW_3j1b_Muon.Fill(Transfer)
        for Transfer in nEta_foward_Jet_3j1b_Muon:
            self.h_nEta_foward_Jet_3j1b_Muon.Fill(Transfer)
        for Transfer in M_light_Jet_3j1b_Muon:
            self.h_M_light_Jet_3j1b_Muon.Fill(Transfer)
        for Transfer in M_Extra_Jet_3j1b_Muon:
            self.h_M_extra_Jet_3j1b_Muon.Fill(Transfer)
        for Transfer in M_b_Jet_3j1b_Muon:
            self.h_M_b_Jet_3j1b_Muon.Fill(Transfer)
        for Transfer in Missing_trasverse_Energy_3j1b_Muon:
            self.h_Missing_3j1b_Muon.Fill(Transfer)
        for Transfer in Helicity_angle_btag_3j1b_Muon:
            self.h_Helicity_btag_3j1b_Muon.Fill(Transfer)
        for Transfer in Helicity_angle_Extra_3j1b_Muon:
            self.h_Helicity_Extra_3j1b_Muon.Fill(Transfer)
        for Transfer in Polarization_angle_btag_3j1b_Muon:
            self.h_Polarization_btag_3j1b_Muon.Fill(Transfer)
        for Transfer in Polarization_angle_Extra_3j1b_Muon:
            self.h_Polarization_Extra_3j1b_Muon.Fill(Transfer)
        for Transfer in Tag_score_btag_Muon:
            self.h_Tag_score_bjet_3j1b_Muon.Fill(Transfer)

        #3j2b event 

        for Transfer in Top_nu_M_3j2b_Muon:
            self.h_Top_M_3j2b_Muon.Fill(Transfer)
        for Transfer in MtW_3j2b_Muon:
            self.h_MtW_3j2b_Muon.Fill(Transfer)
        for Transfer in nEta_foward_Jet_3j2b_Muon:
            self.h_nEta_foward_Jet_3j2b_Muon.Fill(Transfer)
        for Transfer in M_light_Jet_3j2b_Muon:
            self.h_M_light_Jet_3j2b_Muon.Fill(Transfer)
        for Transfer in M_b_Jet_3j2b_Muon:
            self.h_M_b_Jet_3j2b_Muon.Fill(Transfer)
        for Transfer in Missing_trasverse_Energy_3j2b_Muon:
            self.h_Missing_3j2b_Muon.Fill(Transfer)
        for Transfer in Helicity_angle_3j2b_Muon:
            self.h_Helicity_3j2b_Muon.Fill(Transfer)
        for Transfer in Polarization_angle_3j2b_Muon:
            self.h_Polarization_3j2b_Muon.Fill(Transfer)
        for Transfer in Difference_eta_bjet_Muon:
            self.h_Difference_eta_bjet_Muon.Fill(Transfer)


        ####################################################
        ################ELECTRON EVENT######################
        ####################################################


        for Transfer in Top_nu_M_2j1b_Electron:
            self.h_Top_M_2j1b_Electron.Fill(Transfer)
        for Transfer in MtW_2j1b_Electron:
            self.h_MtW_2j1b_Electron.Fill(Transfer)
        for Transfer in nEta_foward_Jet_2j1b_Electron:
            self.h_nEta_2j1b_Electron.Fill(Transfer)
        for Transfer in M_light_Jet_2j1b_Electron:
            self.h_M_light_Jet_2j1b_Electron.Fill(Transfer)
        for Transfer in M_b_Jet_2j1b_Electron:
            self.h_M_b_Jet_2j1b_Electron.Fill(Transfer)
        for Transfer in Missing_trasverse_Energy_2j1b_Electron:
            self.h_Missing_2j1b_Electron.Fill(Transfer)
        for Transfer in Helicity_angle_2j1b_Electron:
            self.h_Helicity_2j1b_Electron.Fill(Transfer)
        for Transfer in Polarization_angle_2j1b_Electron:
            self.h_Polarization_2j1b_Electron.Fill(Transfer)
    

        #3j1b
        for Transfer in Top_nu_M_btag_3j1b_Electron:
            self.h_Top_M_bjet_3j1b_Electron.Fill(Transfer)
        for Transfer in Top_nu_M_extra_3j1b_Electron:
            self.h_Top_M_extra_3j1b_Electron.Fill(Transfer)
        for Transfer in MtW_3j1b_Electron:
            self.h_MtW_3j1b_Electron.Fill(Transfer)
        for Transfer in nEta_foward_Jet_3j1b_Electron:
            self.h_nEta_foward_Jet_3j1b_Electron.Fill(Transfer)
        for Transfer in M_light_Jet_3j1b_Electron:
            self.h_M_light_Jet_3j1b_Electron.Fill(Transfer)
        for Transfer in M_Extra_Jet_3j1b_Electron:
            self.h_M_extra_Jet_3j1b_Electron.Fill(Transfer)
        for Transfer in M_b_Jet_3j1b_Electron:
            self.h_M_b_Jet_3j1b_Electron.Fill(Transfer)
        for Transfer in Missing_trasverse_Energy_3j1b_Electron:
            self.h_Missing_3j1b_Electron.Fill(Transfer)
        for Transfer in Helicity_angle_btag_3j1b_Electron:
            self.h_Helicity_btag_3j1b_Electron.Fill(Transfer)
        for Transfer in Helicity_angle_Extra_3j1b_Electron:
            self.h_Helicity_Extra_3j1b_Electron.Fill(Transfer)
        for Transfer in Polarization_angle_btag_3j1b_Electron:
            self.h_Polarization_btag_3j1b_Electron.Fill(Transfer)
        for Transfer in Polarization_angle_Extra_3j1b_Electron:
            self.h_Polarization_Extra_3j1b_Electron.Fill(Transfer)
        for Transfer in Tag_score_btag_Electron:
            self.h_Tag_score_bjet_3j1b_Electron.Fill(Transfer)

            
        for Transfer in Top_nu_M_3j2b_Electron:
            self.h_Top_M_3j2b_Electron.Fill(Transfer)
        for Transfer in MtW_3j2b_Electron:
            self.h_MtW_3j2b_Electron.Fill(Transfer)
        for Transfer in nEta_foward_Jet_3j2b_Electron:
            self.h_nEta_foward_Jet_3j2b_Electron.Fill(Transfer)
        for Transfer in M_light_Jet_3j2b_Electron:
            self.h_M_light_Jet_3j2b_Electron.Fill(Transfer)
        for Transfer in M_b_Jet_3j2b_Electron:
            self.h_M_b_Jet_3j2b_Electron.Fill(Transfer)
        for Transfer in Missing_trasverse_Energy_3j2b_Electron:
            self.h_Missing_3j2b_Electron.Fill(Transfer)
        for Transfer in Helicity_angle_3j2b_Electron:
            self.h_Helicity_3j2b_Electron.Fill(Transfer)
        for Transfer in Polarization_angle_3j2b_Electron:
            self.h_Polarization_3j2b_Electron.Fill(Transfer)
        for Transfer in Difference_eta_bjet_Electron:
            self.h_Difference_eta_bjet_Electron.Fill(Transfer)
        

        return True                







