import ROOT
import math
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True
#from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.tWb_Analysis.skimtree_utils import *
from .Selection import Selection



class unpacking_tWb(Module):

    """
    def j_origin(jet,genpart):
        #is_jet_ture = False
        for gen in genpart:
            if (deltaR(jet.p4().Eta(),jet.p4().Phi(),gen.p4().Eta(),gen.p4().Phi()) <0.4 and abs(gen.pdgId)==5 and gen.genPartIdxMother_prompt>-1):
                mom = abs(genpart[genPartIdxMother_prompt].pdgId)
                if mom == 6:
                    return 1
                elif mom == 21:
                    return 2
                else:
                    return 3
        return 4#
    """

    def __init__(self):
        #self.isMC = isMC
        #self.selector = Selection()
        #self.writeHistFile = True
        pass
    def beginJob(self):
        pass
        
        
        #Module.beginJob(self,histFile,histDirName)
        #ROOT.gStyle.SetOptStat(1111)
        
        #pass
        
        #Creation of the histo for each category. 

        #2j1b
        """
        #==================================MUON=======================================
        #
        self.h_Top_M_2j1b_Muon = ROOT.TH1F("h_Top_M_2j1b_Muon","Top mass",100,0,1000)
        self.h_MtW_2j1b_Muon = ROOT.TH1F("h_MtW_2j1b_Muon","Wt mass",100,0,1000)
        self.h_nEta_foward_Jet_2j1b_Muon = ROOT.TH1F("h_nEta_2j1b_Muon","Mass_Eta_foward_Jet_Muon",100,0,7)
        self.h_M_light_Jet_2j1b_Muon = ROOT.TH1F("h_M_light_2j1b_Muon","Mass light jet Muon ",100,0,1000)
        self.h_M_b_Jet_2j1b_Muon = ROOT.TH1F("h_M_b_Jet_2j1b_Muon","Mass b jet Muon",100,0,1000)
        self.h_Missing_2j1b_Muon = ROOT.TH1F("h_Missing_Energy_2j1b_Muon","Missing Trasverse Energy",100,0,1000)
        self.h_Helicity_2j1b_Muon = ROOT.TH1F("h_Helicity_2j1b_Muon","Helicity angle 2j1b Muon",100,-1.2,1.2)
        self.h_Polarization_2j1b_Muon = ROOT.TH1F("h_Polarization_2j1b_Muon","Polarization angle 2j1b Muon",100,-1.2,1.2)

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
        self.h_Top_M_2j1b_Electron = ROOT.TH1F("h_Top_M_2j1b_Electron","Top mass",100,0,1000) 
        self.h_MtW_2j1b_Electron = ROOT.TH1F("h_MtW_2j1b_Electron","Wt mass",100,0,1000)
        self.h_nEta_foward_Jet_2j1b_Electron = ROOT.TH1F("h_nEta_2j1b_Electron","Mass_Eta_foward_Jet_Electron",100,0,7)
        self.h_M_light_Jet_2j1b_Electron = ROOT.TH1F("h_M_light_2j1b_Electron","Mass light jet Electron",100,0,1000)
        self.h_M_b_Jet_2j1b_Electron = ROOT.TH1F("h_M_b_Jet_2j1b_Electron","Mass b jet Electron",100,0,1000)
        self.h_Missing_2j1b_Electron = ROOT.TH1F("h_Missing_Energy_2j1b_Electron","Missing Trasverse Energy",100,0,1000)
        self.h_Helicity_2j1b_Electron = ROOT.TH1F("h_Helicity_2j1b_Electron","Helicity angle 2j1b Electron",100,-1.2,1.2)
        self.h_Polarization_2j1b_Electron = ROOT.TH1F("h_Polarization_2j1b_Electron","Polarization angle 2j1b Electron",100,-1.2,1.2)

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
        self.h_Top_M_bjet_3j1b_Muon = ROOT.TH1F("h_Top_M_bjet_3j1b_Muon","",100,0,1000)
        self.h_Top_M_extra_3j1b_Muon = ROOT.TH1F("h_Top_M_extra_3j1b_Muon","",100,0,1000)
        self.h_MtW_3j1b_Muon = ROOT.TH1F("h_MtW_3j1b_Muon","",100,0,1000)
        self.h_nEta_foward_Jet_3j1b_Muon = ROOT.TH1F("h_nEta_foward_Jet_3j1b_Muon","",100,0,7)
        self.h_M_b_Jet_3j1b_Muon = ROOT.TH1F("h_M_b_Jet_3j1b_Muon","",100,0,1000)
        self.h_M_extra_Jet_3j1b_Muon = ROOT.TH1F("h_M_extra_Jet_3j1b_Muon","",100,0,1000)
        self.h_M_light_Jet_3j1b_Muon = ROOT.TH1F("h_M_light_Jet_3j1b_Muon","",100,0,1000)
        self.h_Missing_3j1b_Muon = ROOT.TH1F("h_Missing_3j1b_Muon","",100,0,1000)
        self.h_Helicity_btag_3j1b_Muon = ROOT.TH1F("h_Helicity_btag_3j1b_Muon","",100,-1.5,1.5)
        self.h_Helicity_Extra_3j1b_Muon = ROOT.TH1F("h_Helicity_Extra_3j1b_Muon","",100,-1.5,1.5)
        self.h_Polarization_Extra_3j1b_Muon = ROOT.TH1F("h_Polarization_Extra_3j1b_Muon","",100,-1.5,1.5)
        self.h_Polarization_btag_3j1b_Muon = ROOT.TH1F("h_Polarization_btag_3j1b_Muon","",100,-1.5,1.5)
        self.h_Tag_score_bjet_3j1b_Muon = ROOT.TH1F("h_Tag_score_bjet_3j1b_Muon","",100,-2,2)
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
        self.h_Top_M_bjet_3j1b_Electron = ROOT.TH1F("h_Top_M_bjet_3j1b_Electron","",100,0,1000)
        self.h_Top_M_extra_3j1b_Electron = ROOT.TH1F("h_Top_M_extra_3j1b_Electron","",100,0,1000)
        self.h_MtW_3j1b_Electron = ROOT.TH1F("h_MtW_3j1b_Electron","",100,0,1000)
        self.h_nEta_foward_Jet_3j1b_Electron = ROOT.TH1F("h_nEta_foward_Jet_3j1b_Electron","",100,0,7)
        self.h_M_b_Jet_3j1b_Electron = ROOT.TH1F("h_M_b_Jet_3j1b_Electron","",100,0,1000)
        self.h_M_extra_Jet_3j1b_Electron = ROOT.TH1F("h_M_extra_Jet_3j1b_Electron","",100,0,1000)
        self.h_M_light_Jet_3j1b_Electron = ROOT.TH1F("h_M_light_Jet_3j1b_Electron","",100,0,1000)
        self.h_Missing_3j1b_Electron = ROOT.TH1F("h_Missing_3j1b_Electron","",100,0,1000)
        self.h_Helicity_btag_3j1b_Electron = ROOT.TH1F("h_Helicity_btag_3j1b_Electron","",100,-1.5,1.5)
        self.h_Helicity_Extra_3j1b_Electron = ROOT.TH1F("h_Helicitt_Extra_3j1b_Electron","",100,-1.5,1.5)
        self.h_Polarization_Extra_3j1b_Electron = ROOT.TH1F("h_Polarization_Extra_3j1b_Electron","",100,-1.5,1.5)
        self.h_Polarization_btag_3j1b_Electron = ROOT.TH1F("h_Polarization_btag_3j1b_Electron","",100,-1.5,1.5)
        self.h_Tag_score_bjet_3j1b_Electron = ROOT.TH1F("h_Tag_score_bjet_3j1b_Electron","",100,-2,2)
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
        self.h_Top_M_3j2b_Muon = ROOT.TH1F("h_Top_M_3j2b_Muon","",100,0,1000)
        self.h_MtW_3j2b_Muon = ROOT.TH1F("h_MtW_3j2b_Muon","",100,0,1000)
        self.h_nEta_foward_Jet_3j2b_Muon = ROOT.TH1F("h_nEta_foward_Jet_3j2b_Muon","",100,0,7)
        self.h_M_light_Jet_3j2b_Muon = ROOT.TH1F("h_M_light_Jet_3j2b_Muon","",100,0,1000)
        self.h_M_b_Jet_3j2b_Muon = ROOT.TH1F("h_M_b_Jet_3j2b_Muon","",100,0,1000)
        self.h_Missing_3j2b_Muon = ROOT.TH1F("h_Missing_Energy_3j2b_Muon","",100,0,1000)
        self.h_Helicity_3j2b_Muon = ROOT.TH1F("h_Helicity_3j2b_Muon","",100,-1.5,1.5)
        self.h_Polarization_3j2b_Muon = ROOT.TH1F("h_Polarization_3j2b_Muon","",100,-1.5,1.5)
        self.h_Difference_eta_bjet_Muon = ROOT.TH1F("h_Difference_eta_bjet_Muon","",100,0,10)


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
        self.h_Top_M_3j2b_Electron = ROOT.TH1F("h_Top_M_3j2b_Electron","",100,0,1000)
        self.h_MtW_3j2b_Electron = ROOT.TH1F("h_MtW_3j2b_Electron","",100,0,1000)
        self.h_nEta_foward_Jet_3j2b_Electron = ROOT.TH1F("h_nEta_foward_Jet_3j2b_Electron","",100,0,7)
        self.h_M_light_Jet_3j2b_Electron = ROOT.TH1F("h_M_light_Jet_3j2b_Electron","",100,0,1000)
        self.h_M_b_Jet_3j2b_Electron = ROOT.TH1F("h_M_b_Jet_3j2b_Electron","",100,0,1000)
        self.h_Missing_3j2b_Electron = ROOT.TH1F("h_Missing_Energy_3j2b_Electron","",100,0,1000)
        self.h_Helicity_3j2b_Electron = ROOT.TH1F("h_Helicity_3j2b_Electron","",100,-1.5,1.5)
        self.h_Polarization_3j2b_Electron = ROOT.TH1F("h_Polarization_3j2b_Electron","",100,-1.5,1.5)
        self.h_Difference_eta_bjet_Electron = ROOT.TH1F("h_Difference_eta_bjet_Electron","",100,0,10)

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
        """



    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        #Branch variabili top con nu

        #self.out.branch("Top_nu_pt","F", lenVar="nTop") 
        #self.out.branch("Top_nu_eta","F", lenVar="nTop")
        #self.out.branch("Top_nu_phi","F", lenVar="nTop")
        #self.out.branch("Top_nu_e","F", lenVar="nTop")
        #self.out.branch("Top_nu_M","F", lenVar="nTop")

        
        #---------------------------------------------------------------------------------
        #-----------------------------2j1b category---------------------------------------
        #---------------------------------------------------------------------------------
        self.out.branch("Top_nu_M_2j1b_Electron", "F", lenVar="nTop_2j1b_Electron")
        self.out.branch("Top_nu_M_2j1b_Muon", "F", lenVar="nTop_2j1b_Muon")
        #
        self.out.branch("MtW_2j1b_Electron","F",lenVar="nTopW_2j1b_Electron")
        self.out.branch("MtW_2j1b_Muon","F",lenVar="nTopW_2j1b_Muon")
        #
        self.out.branch("nEta_foward_Jet_2j1b_Electron","F",lenVar="nEta_t_2j1b_Electron")
        self.out.branch("nEta_foward_Jet_2j1b_Muon","F",lenVar="nEta_t_2jb1_Muon")
        #
        self.out.branch("M_light_Jet_2j1b_Electron","F",lenVar = "nM_light_Jet_2j1b_Electron")
        self.out.branch("M_light_Jet_2j1b_Muon","F", lenVar = "mM_light_Jet_2j1b_Muon")
        #
        self.out.branch("M_b_Jet_2j1b_Electron","F",lenVar="nM_b_Jet_2j1b_Electron")
        self.out.branch("M_b_Jet_2j1b_Muon","F",lenVar="nM_b_Jet_2j1b_Muon")
        #
        self.out.branch("Missing_trasverse_Energy_2j1b_Electron","F",lenVar="n_Missing_2j1b_Electron")
        self.out.branch("Missing_trasverse_Energy_2j1b_Muon","F",lenVar="n_Missing_2j1b_Muon")
        #
        self.out.branch("Helicity_angle_2j1b_Electron","F",lenVar="nHelicity_angle_2j1b_Electron")
        self.out.branch("Helicity_angle_2j1b_Muon","F",lenVar="nHelicity_angle_2j1b_Muon")
        #
        self.out.branch("Polarization_angle_2j1b_Electron","F",lenVar="nPolarization_angle_2j1b_Electron")
        self.out.branch("Polarization_angle_2j1b_Muon","F",lenVar="nPolarization_angle_2jb1_Muon")

        #self.out.branch("Jet_tag_born_Muon","I",lenVar="nJet_tag_born_Electron")
        #self.out.branch("Jet_tag_born_Electron","I",lenVar="nJet_tag_born_Muon")

        #-----------------------------------------------------------------------------------
        #---------------------------------3j1b----------------------------------------------
        #-----------------------------------------------------------------------------------
        #
        self.out.branch("Top_nu_M_btag_3j1b_Electron", "F", lenVar="nTop_3j1b_btag_Electron")
        self.out.branch("Top_nu_M_btag_3j1b_Muon", "F", lenVar="nTop_3j1b_btag_Muon")
        #
        self.out.branch("Top_nu_M_extra_3j1b_Electron","F",lenVar="nTop_3j1b_Extra_Electron")
        self.out.branch("Top_nu_M_extra_3j1b_Muon","F",lenVar="nTop_3j1b_Extra_Muon")
        #
        self.out.branch("MtW_3j1b_Electron","F",lenVar="nTopW_3j1b_Electron")
        self.out.branch("MtW_3j1b_Muon","F",lenVar="nTopW_3j1b_Muon")
        #
        self.out.branch("nEta_foward_Jet_3j1b_Electron","F",lenVar="nEta_t_3j1b_Electron")
        self.out.branch("nEta_foward_Jet_3j1b_Muon","F",lenVar="nEta_t_3j1b_Muon")
        #
        self.out.branch("M_light_Jet_3j1b_Electron","F",lenVar = "mM_light_Jet_3j1b_Electron")
        self.out.branch("M_light_Jet_3j1b_Muon","F",lenVar="nM_light_Jet_3j1b_Muon")
        #
        self.out.branch("M_Extra_Jet_3j1b_Electron","F",lenVar="nM_Extra_Jet_3j1b_Electron")
        self.out.branch("M_Extra_Jet_3j1b_Muon","F",lenVar="nM_Extra_Jet_3j1b_Muon")
        #
        self.out.branch("M_b_Jet_3j1b_Electron","F",lenVar="nM_b_Jet_3j1b_Electron")
        self.out.branch("M_b_Jet_3j1b_Muon","F",lenVar="nM_b_Jet_3j1b_Muon")
        #
        self.out.branch("Missing_trasverse_Energy_3j1b_Electron","F",lenVar="n_Missing_3j1b_Electron")
        self.out.branch("Missing_trasverse_Energy_3j1b_Muon","F",lenVar="n_Missing_3j1b_Muon")
        #
        self.out.branch("Helicity_angle_btag_3j1b_Electron","F",lenVar="nHelicity_angle_btag_3j1b_Electron")
        self.out.branch("Helicity_angle_btag_3j1b_Muon","F",lenVar="nHelicity_angle_btag_3j1b_Muon")
        #
        self.out.branch("Helicity_angle_Extra_3j1b_Electron","F",lenVar="nHelicity_angle_Extra_3j1b_Electron")
        self.out.branch("Helicity_angle_Extra_3j1b_Muon","F",lenVar="nHelicity_angle_Extra_3j1b_Muon")
        #
        self.out.branch("Polarization_angle_btag_3j1b_Electron","F",lenVar="nPolarization_angle_3j1b_Electron")
        self.out.branch("Polarization_angle_btag_3j1b_Muon","F",lenVar="nPolaritzation_angle_3j1b_Muon")
        #
        self.out.branch("Polarization_angle_Extra_3j1b_Electron","F",lenVar="nPolarization_angle_Extra_3j1b_Electron")
        self.out.branch("Polarization_angle_Extra_3j1b_Muon","F",lenVar="nPolarization_angle_Extra_3j1b_Muon")

        self.out.branch("Tag_score_btag_Electron","F",lenVar="nTag_b_Electron")
        self.out.branch("Tag_score_btag_Muon","F",lenVar="nTag_b_Muon")

        #--------------------------------------------------------------------------------
        #---------------------------------3j2b-------------------------------------------
        #--------------------------------------------------------------------------------
        self.out.branch("Top_nu_M_3j2b_Electron", "F", lenVar="nTop_3j2b_Electron")
        self.out.branch("Top_nu_M_3j2b_Muon", "F", lenVar="nTop_3j2b_Muon")
        #
        self.out.branch("MtW_3j2b_Electron","F",lenVar= "nTopW_3j2b_Electron")
        self.out.branch("MtW_3j2b_Muon","F",lenVar="nTopW_3j2b_Muon")
        #
        self.out.branch("nEta_foward_Jet_3j2b_Electron","F",lenVar="nEta_t_3j2b_Electron")
        self.out.branch("nEta_foward_Jet_3j2b_Muon","F",lenVar="nEta_t_3j2b_Muon")
        #
        self.out.branch("M_light_Jet_3j2b_Electron","F",lenVar="nM_light_Jet_3j2b_Electron")
        self.out.branch("M_light_Jet_3j2b_Muon","F",lenVar="nM_light_Jet_3j2b_Muon")
        #
        self.out.branch("M_b_Jet_3j2b_Electron","F",lenVar="nM_b_Jet_3j2b_Electron")
        self.out.branch("M_b_Jet_3j2b_Muon","F",lenVar="nM_b_Jet_3j2b_Muon")
        #
        self.out.branch("Missing_trasverse_Energy_3j2b_Electron","F",lenVar="n_Missing_3j2b_Electron")
        self.out.branch("Missing_trasverse_Energy_3j2b_Muon","F",lenVar="n_Missing_3j2b_Muon")
        #
        self.out.branch("Helicity_angle_3j2b_Electron","F",lenVar="nHelicity_angle_3j2b_Electron")
        self.out.branch("Helicity_angle_3j2b_Muon","F",lenVar="nHelicity_angle_3j2b_Muon")
        #
        self.out.branch("Polarization_angle_3j2b_Electron","F",lenVar="nPolarization_angle_3j2b_Electron")
        self.out.branch("Polarization_angle_3j2b_Muon","F",lenVar="nPolarization_angle_3j2b_Muon")
        #
        self.out.branch("Difference_eta_bjet_Electron","F",lenVar="nDifference_eta_bjet_Electron")
        self.out.branch("Difference_eta_bjet_Muon","F",lenVar="nDifference_eta_bjet_Muon")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        electrons = Collection(event, "Electron")
        MET = Object(event, "PuppiMET")
        fatjets = Collection(event, "FatJet")
        """
        if self.isMC==1 :
            genpart = Collection(event, "GenPart")
            LHE = Collection(event, "LHEPart")
        """
        #
        Jet_category = getattr(event, "Jet_eventCategory") 
        Lepton_category = getattr(event, "Lepton_eventCategory")
        
        #Indx value
        tightMuon_idx = getattr(event,"tightMuon_idx")
        tightElectron_idx = getattr(event,"tightElectron_idx")
        goodJets_idx = list(getattr(event, "goodJets_idx"))
        bJets_idx = list(getattr(event, "bJets_idx"))



        #Dichiarazione variabili:
        #Massa del top per categoria
        top_nu_momentum_utils = TopUtilities()
        Top_nu_M_2j1b_Electron = []
        Top_nu_M_2j1b_Muon = []
        Top_nu_M_btag_3j1b_Electron = []
        Top_nu_M_btag_3j1b_Muon = []
        Top_nu_M_extra_3j1b_Electron = []
        Top_nu_M_extra_3j1b_Muon = []
        Top_nu_M_3j2b_Electron = [] 
        Top_nu_M_3j2b_Muon = []


        #Massa trasversa della W:
        MtW_2j1b_Muon = []        
        MtW_2j1b_Electron = []

        MtW_3j1b_Muon = []
        MtW_3j1b_Electron = []

        MtW_3j2b_Muon = []
        MtW_3j2b_Electron = []

        #Foward Eta Jet
        nEta_foward_Jet_2j1b_Electron = [] 
        nEta_foward_Jet_2j1b_Muon = []

        nEta_foward_Jet_3j1b_Electron = []
        nEta_foward_Jet_3j1b_Muon = []

        nEta_foward_Jet_3j2b_Electron = []
        nEta_foward_Jet_3j2b_Muon = []

        #Massa lepton+Foward_Jet
        M_light_Jet_2j1b_Electron = []
        M_light_Jet_2j1b_Muon = []
        M_light_Jet_3j1b_Electron = []
        M_light_Jet_3j1b_Muon = []
        M_light_Jet_3j2b_Electron = []
        M_light_Jet_3j2b_Muon = []

        #Mass lepton+extra_jet 
        M_Extra_Jet_3j1b_Electron = []
        M_Extra_Jet_3j1b_Muon = []


        #Mass lepton+btag jet:
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



        #Genpart 
        #Jen_tag_born_Electron_2j1b = []
        #Jen_tag_born_Muon_2j1b = []


        
        #Define a TLorentz vector for the top candidate
        top_nu_momentum = ROOT.TLorentzVector()
        

        #Using the idx for the recostruction of the top reco 
        #Muon = 1 and Lepton = 2
        #-----MUON EVENTS------
        # Muon, 2j1b
        if Lepton_category == 1 and Jet_category == 1:  # Muon, 2j1b
            mu = muons[tightMuon_idx]

            #Prendi i jet taggati nel file 
            goodJets = [jets[i] for i in goodJets_idx]
            bJets = [jets[i] for i in bJets_idx]

            # identifica i non-b-jet
            non_b_jets = [j for j in goodJets if j not in bJets]
            
            if len(non_b_jets) != 1:
                return False
            
            nEta_foward_Jet_2j1b_Muon.append(abs(non_b_jets[0].eta))


            for b_idx in bJets_idx:
                b = jets[b_idx]
                top_nu_momentum, IsmcNeg, mcdR_lepjet, neutrino = top_nu_momentum_utils.topnu_4Momentum(
                    lepton=mu.p4(),
                    jet=b.p4(),
                    metPx=MET.pt * math.cos(MET.phi),
                    metPy=MET.pt * math.sin(MET.phi)
                )
                if top_nu_momentum:
                    Top_nu_M_2j1b_Muon.append(top_nu_momentum.M())

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

                    if (costheta_star < 1 and costheta_star > -1):
                        Helicity_angle_2j1b_Muon.append(costheta_star)
                    if (cospol_star < 1 and cospol_star > -1):    
                        Polarization_angle_2j1b_Muon.append(cospol_star)


                #Muon+bjet:
                lep_bjet_p4 = mu.p4()+b.p4()
                M_lbj = lep_bjet_p4.M()
                M_b_Jet_2j1b_Muon.append(M_lbj)

                

            #Calcolo massa Trasversa W
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





            
            






        # Muon, 3j1b
        if Lepton_category == 1 and Jet_category == 2:
            mu = muons[tightMuon_idx]
            
            #Prendi i jet taggati nel file 
            goodJets = [jets[i] for i in goodJets_idx]
            bJets = [jets[i] for i in bJets_idx]

            # identifica i non-b-jet
            non_b_jets = [j for j in goodJets if j not in bJets]
            if len(non_b_jets) != 2:
                return False  # skipa l'evento se ci sono più di 2b_jet in questa categoria.

            # seleziona quello con |η| minore
            jet_selected = min(non_b_jets, key=lambda x: abs(x.eta))
            # selezione quello con |η| max
            foward_jet = max(non_b_jets, key = lambda x: abs(x.eta))

            nEta_foward_Jet_3j1b_Muon.append(abs(foward_jet.eta))

            Tag_score_btag_Muon.append(jet_selected.btagUParTAK4B)


            #Ciclo sui b_jet
            for b_idx in bJets_idx:
                b = jets[b_idx]
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




       
        #Muon, 3j2b
        if Lepton_category == 1 and Jet_category == 3:
            mu = muons[tightMuon_idx]
            #Prendi i jet taggati nel file 
            goodJets = [jets[i] for i in goodJets_idx]
            bJets = [jets[i] for i in bJets_idx]

            non_b_jets = [j for j in goodJets if j not in bJets]
            

            if len(non_b_jets)!=1: 
                return False
            
            nEta_foward_Jet_3j2b_Muon.append(abs(non_b_jets[0].eta))
            
            #Difference eta of the two bjet 
            if len(bJets) == 2:
                deltaEta_b = abs(bJets[0].eta-bJets[1].eta)
                Difference_eta_bjet_Muon.append(deltaEta_b)


            for b_idx in bJets_idx:
                b = jets[b_idx]
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


       
        #-----ELECTRON EVENTS---------
        #Electron, 2j1b
        if Lepton_category == 2 and Jet_category == 1:  # Electron, 2j1b
            ele = electrons[tightElectron_idx]
            
            #Prendi i jet taggati nel file 
            goodJets = [jets[i] for i in goodJets_idx]
            bJets = [jets[i] for i in bJets_idx]

            # identifica i non-b-jet
            non_b_jets = [j for j in goodJets if j not in bJets]
            
            if len(non_b_jets) != 1:
                return False
            
            nEta_foward_Jet_2j1b_Electron.append(abs(non_b_jets[0].eta))

            #Ricostruzione top con i bjet taggati
            for b_idx in bJets_idx:
                b = jets[b_idx]
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
        
        
        
        
        # Electron, 3j1b
        if Lepton_category == 2 and Jet_category == 2:
            ele = electrons[tightElectron_idx]
            
            #Prendi i jet taggati nel file 
            goodJets = [jets[i] for i in goodJets_idx]
            bJets = [jets[i] for i in bJets_idx]

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



            for b_idx in bJets_idx:
                b = jets[b_idx]
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
       



        # Electron, 3j2b        
        if Lepton_category == 2 and Jet_category == 3:
            ele = electrons[tightElectron_idx]
            
            goodJets = [jets[i] for i in goodJets_idx]
            bJets = [jets[i] for i in bJets_idx]

            non_b_jets = [j for j in goodJets if j not in bJets]
            

            
            if len(non_b_jets)!=1: 
                return False
            
            nEta_foward_Jet_3j2b_Electron.append(abs(non_b_jets[0].eta))
            
            #Difference eta of the two bjet 
            if len(bJets) == 2:
                deltaEta_b = abs(bJets[0].eta-bJets[1].eta)
                Difference_eta_bjet_Electron.append(deltaEta_b)


            
            for b_idx in bJets_idx:
                b = jets[b_idx]
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
       



        # ---- FILL DELLE BRANCH ----
        
        #Fill the mass of the top for each category 
        self.out.fillBranch("Top_nu_M_2j1b_Electron", Top_nu_M_2j1b_Electron)
        self.out.fillBranch("Top_nu_M_2j1b_Muon", Top_nu_M_2j1b_Muon)
        self.out.fillBranch("Top_nu_M_btag_3j1b_Electron",Top_nu_M_btag_3j1b_Electron)
        self.out.fillBranch("Top_nu_M_btag_3j1b_Muon",Top_nu_M_btag_3j1b_Muon)
        self.out.fillBranch("Top_nu_M_extra_3j1b_Electron",Top_nu_M_extra_3j1b_Electron)
        self.out.fillBranch("Top_nu_M_extra_3j1b_Muon",Top_nu_M_extra_3j1b_Muon)
        self.out.fillBranch("Top_nu_M_3j2b_Electron", Top_nu_M_3j2b_Electron)
        self.out.fillBranch("Top_nu_M_3j2b_Muon", Top_nu_M_3j2b_Muon)

        #Fill the trasverse mass of the W. 
        self.out.fillBranch("MtW_2j1b_Electron",MtW_2j1b_Electron)
        self.out.fillBranch("MtW_2j1b_Muon",MtW_2j1b_Muon)
        self.out.fillBranch("MtW_3j1b_Electron",MtW_3j1b_Electron)
        self.out.fillBranch("MtW_3j1b_Muon",MtW_3j1b_Muon)
        self.out.fillBranch("MtW_3j2b_Electron",MtW_3j2b_Electron)
        self.out.fillBranch("MtW_3j2b_Muon",MtW_3j2b_Muon)
        
        #Fill the nEta from the light Jet
        self.out.fillBranch("nEta_foward_Jet_2j1b_Electron",nEta_foward_Jet_2j1b_Electron)
        self.out.fillBranch("nEta_foward_Jet_2j1b_Muon",nEta_foward_Jet_2j1b_Muon)
        self.out.fillBranch("nEta_foward_Jet_3j1b_Electron",nEta_foward_Jet_3j1b_Electron)
        self.out.fillBranch("nEta_foward_Jet_3j1b_Muon",nEta_foward_Jet_3j1b_Muon)
        self.out.fillBranch("nEta_foward_Jet_3j2b_Electron",nEta_foward_Jet_3j2b_Electron)
        self.out.fillBranch("nEta_foward_Jet_3j2b_Muon",nEta_foward_Jet_3j2b_Muon)

        #Fill the different masses for each event:
        self.out.fillBranch("M_light_Jet_2j1b_Electron",M_light_Jet_2j1b_Electron)
        self.out.fillBranch("M_light_Jet_2j1b_Muon",M_light_Jet_2j1b_Muon)
        self.out.fillBranch("M_light_Jet_3j1b_Electron",M_light_Jet_3j1b_Electron)
        self.out.fillBranch("M_light_Jet_3j1b_Muon",M_light_Jet_3j1b_Muon)
        self.out.fillBranch("M_light_Jet_3j2b_Electron",M_light_Jet_3j2b_Electron)
        self.out.fillBranch("M_light_Jet_3j2b_Muon",M_light_Jet_3j2b_Muon)
        self.out.fillBranch("M_Extra_Jet_3j1b_Electron",M_Extra_Jet_3j1b_Electron)
        self.out.fillBranch("M_Extra_Jet_3j1b_Muon",M_Extra_Jet_3j1b_Muon)
        self.out.fillBranch("M_b_Jet_2j1b_Electron",M_b_Jet_2j1b_Electron)
        self.out.fillBranch("M_b_Jet_2j1b_Muon",M_b_Jet_2j1b_Muon)
        self.out.fillBranch("M_b_Jet_3j1b_Electron",M_b_Jet_3j1b_Electron)
        self.out.fillBranch("M_b_Jet_3j1b_Muon",M_b_Jet_3j1b_Muon)
        self.out.fillBranch("M_b_Jet_3j2b_Electron",M_b_Jet_3j2b_Electron)
        self.out.fillBranch("M_b_Jet_3j2b_Muon",M_b_Jet_3j2b_Muon)

        #Fill the missing trasverse Energy for each :
        self.out.fillBranch("Missing_trasverse_Energy_2j1b_Electron",Missing_trasverse_Energy_2j1b_Electron)
        self.out.fillBranch("Missing_trasverse_Energy_2j1b_Muon",Missing_trasverse_Energy_2j1b_Muon)
        self.out.fillBranch("Missing_trasverse_Energy_3j1b_Electron",Missing_trasverse_Energy_3j1b_Electron)
        self.out.fillBranch("Missing_trasverse_Energy_3j1b_Muon",Missing_trasverse_Energy_3j1b_Muon)
        self.out.fillBranch("Missing_trasverse_Energy_3j2b_Electron",Missing_trasverse_Energy_3j2b_Electron)
        self.out.fillBranch("Missing_trasverse_Energy_3j2b_Muon",Missing_trasverse_Energy_3j2b_Muon)

     
        #Fill the Helicity Branch 
        self.out.fillBranch("Helicity_angle_2j1b_Electron",Helicity_angle_2j1b_Electron)   
        self.out.fillBranch("Helicity_angle_2j1b_Muon",Helicity_angle_2j1b_Muon)
        self.out.fillBranch("Helicity_angle_btag_3j1b_Electron",Helicity_angle_btag_3j1b_Electron)
        self.out.fillBranch("Helicity_angle_btag_3j1b_Muon",Helicity_angle_btag_3j1b_Muon)
        self.out.fillBranch("Helicity_angle_Extra_3j1b_Electron",Helicity_angle_Extra_3j1b_Electron)
        self.out.fillBranch("Helicity_angle_Extra_3j1b_Muon",Helicity_angle_Extra_3j1b_Muon)
        self.out.fillBranch("Helicity_angle_3j2b_Electron",Helicity_angle_3j2b_Electron)
        self.out.fillBranch("Helicity_angle_3j2b_Muon",Helicity_angle_3j2b_Muon)
     
        #Fill the polarization Branch 
        self.out.fillBranch("Polarization_angle_2j1b_Electron",Polarization_angle_2j1b_Electron)
        self.out.fillBranch("Polarization_angle_2j1b_Muon",Polarization_angle_2j1b_Muon)
        self.out.fillBranch("Polarization_angle_btag_3j1b_Electron",Polarization_angle_btag_3j1b_Electron)
        self.out.fillBranch("Polarization_angle_btag_3j1b_Muon",Polarization_angle_btag_3j1b_Muon)
        self.out.fillBranch("Polarization_angle_Extra_3j1b_Electron",Polarization_angle_Extra_3j1b_Electron)
        self.out.fillBranch("Polarization_angle_Extra_3j1b_Muon",Polarization_angle_Extra_3j1b_Muon)
        self.out.fillBranch("Polarization_angle_3j2b_Electron",Polarization_angle_3j2b_Electron)
        self.out.fillBranch("Polarization_angle_3j2b_Muon",Polarization_angle_3j2b_Muon)

        #Fill the difference with eta of bJet
        self.out.fillBranch("Difference_eta_bjet_Electron",Difference_eta_bjet_Electron)
        self.out.fillBranch("Difference_eta_bjet_Muon",Difference_eta_bjet_Muon)

        #Fill the tag of Upar for the Extra jet 
        self.out.fillBranch("Tag_score_btag_Electron",Tag_score_btag_Electron)
        self.out.fillBranch("Tag_score_btag_Muon",Tag_score_btag_Muon)

        
        """
        #FILL THE HISTO 


        #=================================MUON=============================================

        #2j1b
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
        #3j2b
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
        
        #========================ELECTRON=================================
        #2j1b
        
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

        #3j2b

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
        
        """























        return True





        
