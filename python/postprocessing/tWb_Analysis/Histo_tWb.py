import ROOT
import math
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True
import sys 
#from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.tWb_Analysis.skimtree_utils import *
from .Selection import Selection


class Histo_tWb(Module):
    def __init__(self):
        self.writeHistFile = True
        #pass
    
    def beginJob(self,histFile= None,histDirName= None):
        Module.beginJob(self,histFile,histDirName)

        #Creation of the histo for each category. 

        #2j1b

        #==================================MUON=======================================
        #
        self.h_Top_M_2j1b_Muon = ROOT.TH1F("h_Top_M_2j1b_Muon","Top mass",17,60,500)
        self.h_MtW_2j1b_Muon = ROOT.TH1F("h_MtW_2j1b_Muon","Wt mass",17,0,250)
        self.h_nEta_foward_Jet_2j1b_Muon = ROOT.TH1F("h_nEta_2j1b_Muon","Eta_foward_Jet_Muon",10,0,4.5)
        self.h_M_light_Jet_2j1b_Muon = ROOT.TH1F("h_M_light_2j1b_Muon","Mass light jet Muon ",20,0,350)
        self.h_M_b_Jet_2j1b_Muon = ROOT.TH1F("h_M_b_Jet_2j1b_Muon","Mass b jet Muon",20,0,350)
        self.h_Missing_2j1b_Muon = ROOT.TH1F("h_Missing_Energy_2j1b_Muon","Missing Trasverse Energy",20,0,200)
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
        self.h_Top_M_2j1b_Electron = ROOT.TH1F("h_Top_M_2j1b_Electron","Top mass",17,60,500) 
        self.h_MtW_2j1b_Electron = ROOT.TH1F("h_MtW_2j1b_Electron","Wt mass",17,0,250)
        self.h_nEta_foward_Jet_2j1b_Electron = ROOT.TH1F("h_nEta_2j1b_Electron","Mass_Eta_foward_Jet_Electron",10,0,4.5)
        self.h_M_light_Jet_2j1b_Electron = ROOT.TH1F("h_M_light_2j1b_Electron","Mass light jet Electron",20,0,350)
        self.h_M_b_Jet_2j1b_Electron = ROOT.TH1F("h_M_b_Jet_2j1b_Electron","Mass b jet Electron",20,0,350)
        self.h_Missing_2j1b_Electron = ROOT.TH1F("h_Missing_Energy_2j1b_Electron","Missing Trasverse Energy",20,0,200)
        self.h_Helicity_2j1b_Electron = ROOT.TH1F("h_Helicity_2j1b_Electron","Helicity angle 2j1b Electron",15,-1,1)
        self.h_Polarization_2j1b_Electron = ROOT.TH1F("h_Polarization_2j1b_Electron","Polarization angle 2j1b Electron",15,-1,1)

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


        #3j1b
        #==================================MUON=========================================
        ##
        self.h_Top_M_bjet_3j1b_Muon = ROOT.TH1F("h_Top_M_bjet_3j1b_Muon","",17,60,500)
        self.h_Top_M_extra_3j1b_Muon = ROOT.TH1F("h_Top_M_extra_3j1b_Muon","",17,60,500)
        self.h_MtW_3j1b_Muon = ROOT.TH1F("h_MtW_3j1b_Muon","",17,0,250)
        self.h_nEta_foward_Jet_3j1b_Muon = ROOT.TH1F("h_nEta_foward_Jet_3j1b_Muon","",10,0,4.5)
        self.h_M_b_Jet_3j1b_Muon = ROOT.TH1F("h_M_b_Jet_3j1b_Muon","",20,0,350)
        self.h_M_extra_Jet_3j1b_Muon = ROOT.TH1F("h_M_extra_Jet_3j1b_Muon","",20,0,350)
        self.h_M_light_Jet_3j1b_Muon = ROOT.TH1F("h_M_light_Jet_3j1b_Muon","",20,0,350)
        self.h_Missing_3j1b_Muon = ROOT.TH1F("h_Missing_3j1b_Muon","",20,0,200)
        self.h_Helicity_btag_3j1b_Muon = ROOT.TH1F("h_Helicity_btag_3j1b_Muon","",15,-1,1)
        self.h_Helicity_Extra_3j1b_Muon = ROOT.TH1F("h_Helicity_Extra_3j1b_Muon","",15,-1,1)
        self.h_Polarization_Extra_3j1b_Muon = ROOT.TH1F("h_Polarization_Extra_3j1b_Muon","",15,-1,1)
        self.h_Polarization_btag_3j1b_Muon = ROOT.TH1F("h_Polarization_btag_3j1b_Muon","",15,-1,1)
        self.h_Tag_score_bjet_3j1b_Muon = ROOT.TH1F("h_Tag_score_bjet_3j1b_Muon","",10,-1,1)
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


        #=================================ELECTRON======================================
        self.h_Top_M_bjet_3j1b_Electron = ROOT.TH1F("h_Top_M_bjet_3j1b_Electron","",17,60,500)
        self.h_Top_M_extra_3j1b_Electron = ROOT.TH1F("h_Top_M_extra_3j1b_Electron","",17,60,500)
        self.h_MtW_3j1b_Electron = ROOT.TH1F("h_MtW_3j1b_Electron","",17,0,250)
        self.h_nEta_foward_Jet_3j1b_Electron = ROOT.TH1F("h_nEta_foward_Jet_3j1b_Electron","",10,0,4.5)
        self.h_M_b_Jet_3j1b_Electron = ROOT.TH1F("h_M_b_Jet_3j1b_Electron","",20,0,350)
        self.h_M_extra_Jet_3j1b_Electron = ROOT.TH1F("h_M_extra_Jet_3j1b_Electron","",20,0,350)
        self.h_M_light_Jet_3j1b_Electron = ROOT.TH1F("h_M_light_Jet_3j1b_Electron","",20,0,350)
        self.h_Missing_3j1b_Electron = ROOT.TH1F("h_Missing_3j1b_Electron","",20,0,200)
        self.h_Helicity_btag_3j1b_Electron = ROOT.TH1F("h_Helicity_btag_3j1b_Electron","",15,-1,1)
        self.h_Helicity_Extra_3j1b_Electron = ROOT.TH1F("h_Helicitt_Extra_3j1b_Electron","",15,-1,1)
        self.h_Polarization_Extra_3j1b_Electron = ROOT.TH1F("h_Polarization_Extra_3j1b_Electron","",15,-1,1)
        self.h_Polarization_btag_3j1b_Electron = ROOT.TH1F("h_Polarization_btag_3j1b_Electron","",15,-1,1)
        self.h_Tag_score_bjet_3j1b_Electron = ROOT.TH1F("h_Tag_score_bjet_3j1b_Electron","",10,-1,1)
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
        self.addObject(self.h_Polarization_Extra_3j1b_Electron)
        self.addObject(self.h_Polarization_btag_3j1b_Electron)
        self.addObject(self.h_Tag_score_bjet_3j1b_Electron)
        ##


        #3j2b
        #===================================MUON=============================================
        self.h_Top_M_3j2b_Muon = ROOT.TH1F("h_Top_M_3j2b_Muon","",17,60,500)
        self.h_MtW_3j2b_Muon = ROOT.TH1F("h_MtW_3j2b_Muon","",17,0,250)
        self.h_nEta_foward_Jet_3j2b_Muon = ROOT.TH1F("h_nEta_foward_Jet_3j2b_Muon","",10,0,4.5)
        self.h_M_light_Jet_3j2b_Muon = ROOT.TH1F("h_M_light_Jet_3j2b_Muon","",20,0,350)
        self.h_M_b_Jet_3j2b_Muon = ROOT.TH1F("h_M_b_Jet_3j2b_Muon","",20,0,350)
        self.h_Missing_3j2b_Muon = ROOT.TH1F("h_Missing_Energy_3j2b_Muon","",20,0,200)
        self.h_Helicity_3j2b_Muon = ROOT.TH1F("h_Helicity_3j2b_Muon","",15,-1,1)
        self.h_Polarization_3j2b_Muon = ROOT.TH1F("h_Polarization_3j2b_Muon","",15,-1,1)
        self.h_Difference_eta_bjet_Muon = ROOT.TH1F("h_Difference_eta_bjet_Muon","",10,0,5)


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
        self.h_Top_M_3j2b_Electron = ROOT.TH1F("h_Top_M_3j2b_Electron","",17,60,500)
        self.h_MtW_3j2b_Electron = ROOT.TH1F("h_MtW_3j2b_Electron","",17,0,250)
        self.h_nEta_foward_Jet_3j2b_Electron = ROOT.TH1F("h_nEta_foward_Jet_3j2b_Electron","",10,0,4.5)
        self.h_M_light_Jet_3j2b_Electron = ROOT.TH1F("h_M_light_Jet_3j2b_Electron","",20,0,350)
        self.h_M_b_Jet_3j2b_Electron = ROOT.TH1F("h_M_b_Jet_3j2b_Electron","",20,0,350)
        self.h_Missing_3j2b_Electron = ROOT.TH1F("h_Missing_Energy_3j2b_Electron","",20,0,200)
        self.h_Helicity_3j2b_Electron = ROOT.TH1F("h_Helicity_3j2b_Electron","",15,-1,1)
        self.h_Polarization_3j2b_Electron = ROOT.TH1F("h_Polarization_3j2b_Electron","",15,-1,1)
        self.h_Difference_eta_bjet_Electron = ROOT.TH1F("h_Difference_eta_bjet_Electron","",10,0,5)

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
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        MET = Object(event, "PuppiMET")
        jets = Collection(event,"Jet")

        #Category branch 
        Jet_category = getattr(event,"Jet_eventCategory")
        Lepton_category = getattr(event,"Lepton_eventCategory")

        #Indx values
        tightMuon_idx = getattr(event,"tightMuon_idx")
        tightElectron_idx = getattr(event,"tightElectron_idx")
        goodJets_idx = list(getattr(event, "goodJets_idx"))
        bJets_idx = list(getattr(event, "bJets_idx"))

        #======================================================
        #====================MUON EVENT========================
        #======================================================
        
        #Muon,2j1b:
        if Lepton_category == 1 and Jet_category == 1:
            
            #==================BRANCH EVENT==============================
            Top_nu_M_2j1b_Muon = list(getattr(event,"Top_nu_M_2j1b_Muon"))
            MtW_2j1b_Muon = list(getattr(event,"MtW_2j1b_Muon"))
            nEta_foward_Jet_2j1b_Muon = list(getattr(event,"nEta_foward_Jet_2j1b_Muon"))
            M_light_Jet_2j1b_Muon = list(getattr(event,"M_light_Jet_2j1b_Muon"))
            M_b_Jet_2j1b_Muon = list(getattr(event,"M_b_Jet_2j1b_Muon"))
            Missing_trasverse_Energy_2j1b_Muon = list(getattr(event,"Missing_trasverse_Energy_2j1b_Muon"))
            Helicity_angle_2j1b_Muon = list(getattr(event,"Helicity_angle_2j1b_Muon"))
            Polarization_angle_2j1b_Muon = list(getattr(event,"Polarization_angle_2j1b_Muon"))


            #FILL HISTO WITH CATEGORY BRANCH
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
                
        #Muon 3j1b:

        if Lepton_category == 1 and Jet_category == 2:

            #=============BRANCH EVENT===================
            Top_nu_M_btag_3j1b_Muon = list(getattr(event,"Top_nu_M_btag_3j1b_Muon"))
            Top_nu_M_extra_3j1b_Muon = list(getattr(event,"Top_nu_M_extra_3j1b_Muon"))
            MtW_3j1b_Muon = list(getattr(event,"MtW_3j1b_Muon"))
            nEta_foward_Jet_3j1b_Muon = list(getattr(event,"nEta_foward_Jet_3j1b_Muon"))
            M_light_Jet_3j1b_Muon = list(getattr(event,"M_light_Jet_3j1b_Muon"))
            M_Extra_Jet_3j1b_Muon = list(getattr(event,"M_Extra_Jet_3j1b_Muon"))
            M_b_Jet_3j1b_Muon = list(getattr(event,"M_b_Jet_3j1b_Muon"))
            Missing_trasverse_Energy_3j1b_Muon = list(getattr(event,"Missing_trasverse_Energy_3j1b_Muon"))
            Helicity_angle_btag_3j1b_Muon = list(getattr(event,"Helicity_angle_btag_3j1b_Muon"))
            Helicity_angle_Extra_3j1b_Muon = list(getattr(event,"Helicity_angle_Extra_3j1b_Muon"))
            Polarization_angle_btag_3j1b_Muon = list(getattr(event,"Polarization_angle_btag_3j1b_Muon"))
            Polarization_angle_Extra_3j1b_Muon = list(getattr(event,"Polarization_angle_Extra_3j1b_Muon"))
            Tag_score_btag_Muon = list(getattr(event,"Tag_score_btag_Muon"))

            #3j1b
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
            
        #Muon 3j2b:
        
        if Lepton_category == 1 and Jet_category == 3:


            
            #===================BRANCH EVENT======================
            Top_nu_M_3j2b_Muon = list(getattr(event,"Top_nu_M_3j2b_Muon"))
            MtW_3j2b_Muon = list(getattr(event,"MtW_3j2b_Muon"))
            nEta_foward_Jet_3j2b_Muon = list(getattr(event,"nEta_foward_Jet_3j2b_Muon"))
            M_light_Jet_3j2b_Muon = list(getattr(event,"M_light_Jet_3j2b_Muon"))
            M_b_Jet_3j2b_Muon = list(getattr(event,"M_b_Jet_3j2b_Muon"))
            Missing_trasverse_Energy_3j2b_Muon = list(getattr(event,"Missing_trasverse_Energy_3j2b_Muon"))
            Helicity_angle_3j2b_Muon = list(getattr(event,"Helicity_angle_3j2b_Muon"))
            Polarization_angle_3j2b_Muon = list(getattr(event,"Polarization_angle_3j2b_Muon"))
            Difference_eta_bjet_Muon = list(getattr(event,"Difference_eta_bjet_Muon"))

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


            
        
        #==========================================================================
        #========================ELECTRON EVENTS===================================
        #==========================================================================

        #Electron 2j1b:

        if Lepton_category == 2 and Jet_category == 1:


            #==================BRANCH EVENT==============================
            Top_nu_M_2j1b_Electron = list(getattr(event,"Top_nu_M_2j1b_Electron"))
            MtW_2j1b_Electron = list(getattr(event,"MtW_2j1b_Electron"))
            nEta_foward_Jet_2j1b_Electron = list(getattr(event,"nEta_foward_Jet_2j1b_Electron"))
            M_light_Jet_2j1b_Electron = list(getattr(event,"M_light_Jet_2j1b_Electron"))
            M_b_Jet_2j1b_Electron = list(getattr(event,"M_b_Jet_2j1b_Electron"))
            Missing_trasverse_Energy_2j1b_Electron = list(getattr(event,"Missing_trasverse_Energy_2j1b_Electron"))
            Helicity_angle_2j1b_Electron = list(getattr(event,"Helicity_angle_2j1b_Electron"))
            Polarization_angle_2j1b_Electron = list(getattr(event,"Polarization_angle_2j1b_Electron"))


            #FILL HISTO WITH CATEGORY BRANCH
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
        
        #Electron 3j1b:

        if Lepton_category == 2 and Jet_category == 2:

            #=============BRANCH EVENT===================
            Top_nu_M_btag_3j1b_Electron = list(getattr(event,"Top_nu_M_btag_3j1b_Electron"))
            Top_nu_M_extra_3j1b_Electron = list(getattr(event,"Top_nu_M_extra_3j1b_Electron"))
            MtW_3j1b_Electron = list(getattr(event,"MtW_3j1b_Electron"))
            nEta_foward_Jet_3j1b_Electron = list(getattr(event,"nEta_foward_Jet_3j1b_Electron"))
            M_light_Jet_3j1b_Electron = list(getattr(event,"M_light_Jet_3j1b_Electron"))
            M_Extra_Jet_3j1b_Electron = list(getattr(event,"M_Extra_Jet_3j1b_Electron"))
            M_b_Jet_3j1b_Electron = list(getattr(event,"M_b_Jet_3j1b_Electron"))
            Missing_trasverse_Energy_3j1b_Electron = list(getattr(event,"Missing_trasverse_Energy_3j1b_Electron"))
            Helicity_angle_btag_3j1b_Electron = list(getattr(event,"Helicity_angle_btag_3j1b_Electron"))
            Helicity_angle_Extra_3j1b_Electron = list(getattr(event,"Helicity_angle_Extra_3j1b_Electron"))
            Polarization_angle_btag_3j1b_Electron = list(getattr(event,"Polarization_angle_btag_3j1b_Electron"))
            Polarization_angle_Extra_3j1b_Electron = list(getattr(event,"Polarization_angle_Extra_3j1b_Electron"))
            Tag_score_btag_Electron = list(getattr(event,"Tag_score_btag_Electron"))


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

            
        #Electron 3j2b:

        if Lepton_category == 2 and Jet_category == 3:

            #===================BRANCH EVENT======================
            Top_nu_M_3j2b_Electron = list(getattr(event,"Top_nu_M_3j2b_Electron"))
            MtW_3j2b_Electron = list(getattr(event,"MtW_3j2b_Electron"))
            nEta_foward_Jet_3j2b_Electron = list(getattr(event,"nEta_foward_Jet_3j2b_Electron"))
            M_light_Jet_3j2b_Electron = list(getattr(event,"M_light_Jet_3j2b_Electron"))
            M_b_Jet_3j2b_Electron = list(getattr(event,"M_b_Jet_3j2b_Electron"))
            Missing_trasverse_Energy_3j2b_Electron = list(getattr(event,"Missing_trasverse_Energy_3j2b_Electron"))
            Helicity_angle_3j2b_Electron = list(getattr(event,"Helicity_angle_3j2b_Electron"))
            Polarization_angle_3j2b_Electron = list(getattr(event,"Polarization_angle_3j2b_Electron"))
            Difference_eta_bjet_Electron = list(getattr(event,"Difference_eta_bjet_Electron"))



            #FILL HISTO WITH CATEGORY BRANCH

            for Transfer in Top_nu_M_3j2b_Electron:
                self.h_Top_M_3j2b_Electron.Fill(Transfer)
            for Transfer in MtW_3j2b_Electron:
                self.h_MtW_3j2b_Electron.Fill(Transfer)
            for Transfer in nEta_foward_Jet_3j2b_Electron:
                self.h_nEta_foward_Jet_3j2b_Electron.Fill(Transfer)
            for Transfer in M_light_Jet_3j2b_Electron:
                self.h_M_light_Jet_3j2b_Electron.Fill(Transfesr)
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
                
        
