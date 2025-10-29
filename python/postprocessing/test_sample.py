import ROOT
import os
#import json_reader as jr

path = os.path.dirname(os.path.abspath(__file__))

class sample:
    def __init__(self, color, style, fill, leglabel, label):
        self.color = color
        self.style = style
        self.fill = fill
        self.leglabel = leglabel
        self.label = label



##########################################################################
################################2024######################################
##########################################################################

################TT_semileptonic#############################
TT_semilep_2024             = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2024")
TT_semilep_2024.sigma       = 762.1 #pb
TT_semilep_2024.year        = 2024
TT_semilep_2024.dataset     = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TT_semilep_2024.process     = "TT_2024"
TT_semilep_2024.unix_code   = 31100
TT_semilep_2024.EE          = 0

TT_semilep_2024_Btag = sample(ROOT.kRed,1,1001,"t#bar{t}", "TT_semilep_2024_Btag") 
TT_semilep_2024_Btag.sigma = 762.1 #pb
TT_semilep_2024_Btag.year = 2024
TT_semilep_2024_Btag.dataset = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-BTVNanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM"
TT_semilep_2024_Btag.process = "TT_semilep_2024_Btag"
TT_semilep_2024_Btag.unix_code = 31101
TT_semilep_2024_Btag.EE = 0


TT_semilep_2024_METjet = sample(ROOT.kRed,1,1001,"t#bar{t}", "TT_semilep_2024_METjet")
TT_semilep_2024_METjet.sigma = 762.1 #pb
TT_semilep_2024_METjet.year = 2024
TT_semilep_2024_METjet.dataset = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM"
TT_semilep_2024_METjet.process = "TT_semilep_2024_METjet"
TT_semilep_2024_METjet.unix_code = 31102
TT_semilep_2024_METjet.EE = 0


TT_2024_semilep                     = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_2024")
TT_2024_semilep.year                = 2024
TT_2024_semilep.components          = [TT_semilep_2024,TT_semilep_2024_Btag,TT_semilep_2024_METjet]



#################################TT_Dileptonic#######################################################
TT_Dileptonic_2024 = sample(ROOT.kRed,1,1003,"tt#bar_{dipleptoni}","TT_Bar_Dilpetonic_2024")
TT_Dileptonic_2024.sigma = 762.1#pb
TT_Dileptonic_2024.year = 2024
TT_Dileptonic_2024.dataset = "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"
TT_Dileptonic_2024.process = "TT_Dileptonic_2024"
TT_Dileptonic_2024.unix_code = 31105
TT_Dileptonic_2024.EE = 0

TT_2024_Dileptonic                       = sample(ROOT.kBlack, 1, 1003, "tt#bar_{dileptonic}","TT_Bar_Dilpetonic_2024")
TT_2024_Dileptonic.year                  = 2024
TT_2024_Dileptonic.components            = [TT_Dileptonic_2024]

##################################Signal_sample###########################################################
tWb_Signal_4FS_T = sample(ROOT.kGreen,1,1002,"t#bar{t}","TBbarQ")
tWb_Signal_4FS_T.sigma = 38.6 #pb
tWb_Signal_4FS_T.year = 2024
tWb_Signal_4FS_T.dataset = "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" 
tWb_Signal_4FS_T.process = "TBbarQ"
tWb_Signal_4FS_T.unix_code = 31103
tWb_Signal_4FS_T.EE = 0


tWb_Signal_4FS_T_bar = sample(ROOT.kGreen,1,1002,"t#bar{t}","TbarBQ")
tWb_Signal_4FS_T_bar.sigma = 23.34 #pb 
tWb_Signal_4FS_T_bar.year = 2024
tWb_Signal_4FS_T_bar.dataset = "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
tWb_Signal_4FS_T_bar.process = "TbarBQ"
tWb_Signal_4FS_T_bar.unix_code = 31104
tWb_Signal_4FS_T_bar.EE = 0 

tWb_Signal_4FS = sample(ROOT.kGreen,1,1002,"t#{t}","tWb_Signal_4FS")
tWb_Signal_4FS.year = 2024
tWb_Signal_4FS.components = [tWb_Signal_4FS_T,tWb_Signal_4FS_T_bar]





















#################################W+jets##################################################










































#==========================SAMPLE DICT=================================================
sample_dict ={




}









