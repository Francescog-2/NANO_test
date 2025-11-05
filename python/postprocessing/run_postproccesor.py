import os, sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.tWb_Analysis.Selection import *
from PhysicsTools.NanoAODTools.postprocessing.tWb_Analysis.unpacking_tWb import *
from PhysicsTools.NanoAODTools.postprocessing.Events_module import*
from PhysicsTools.NanoAODTools.postprocessing.Histo_counts import*
from PhysicsTools.NanoAODTools.postprocessing.tWb_Analysis.JetvetoModule import *
from PhysicsTools.NanoAODTools.postprocessing.tWb_Analysis.Selection_v2 import *

#from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
#from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
#from PhysicsTools.NanoAODTools.postprocessing.tools import *




fnames = [sys.argv[1]]
final_name = sys.argv[2]
outname = sys.argv[3]
label = sys.argv[4]
folder_histo_count = sys.argv[5]
folder_histo_events = sys.argv[6]
label_name = sys.argv[7]

#preselection = "Jet_pt[0] > 40"

"""
p = PostProcessor(
    "/eos/user/f/fconfort/NanoAOD_outputs/tWb_Analysis_TTbar_Semilep", #
    fnames,         # lista di file da processare
    #cut=preselection,    # cut pretaglio
    branchsel=None,      # selezione dei branch (None prende tutti)
    modules=[Selection(),unpacking_tWb()],  # modulo che applica la selezione tight/veto e che restituisce la branch del Mt.
    noOut=False,         # crea anche il file di output con gli eventi
    histFileName="/eos/user/f/fconfort/NanoAOD_outputs/histoEvent_Signal_tWb_Counts/histOut_"+label+".root",
    #histFileName="histSignal.root",
    histDirName="Events",                  
    provenance=True,
    #maxEntries=1000
)
"""
#p.run()

#os.makedirs("/eos/user/f/fconfort/NanoAOD_outputs/tWb_Analysis_TbarBQ_Count",exist_ok=True)

#output_folder_count = "/eos/user/f/fconfort/NanoAOD_outputs/" + folder_histo_count + label
#os.makedirs(output_folder_count, exist_ok=True)

"""
# Job 1: conta eventi:
p_counts = PostProcessor(
    ".",
    fnames,
    modules=[Histo_counts()],
    histFileName=output_folder_count+f"/histo_{label_name}_Count.root",
    histDirName="Events",
    provenance = True,  
    noOut = True    
)


p_counts.run()


#os.makedirs("/eos/user/f/fconfort/NanoAOD_outputs/tWb_Analysis_W+2Jets_Ele_1",exist_ok=True)
#preselection = "Jet_pt[0] > 40"
"""

output_analysis = "/eos/user/f/fconfort/NanoAOD_outputs/" + folder_histo_events + label
os.makedirs(output_analysis, exist_ok= True)



# Job 2: istogrammi fisici
p_vars = PostProcessor(
    "/eos/user/f/fconfort/NanoAOD_outputs/" + folder_histo_events,
    fnames,
    #cut = preselection,
    modules=[Selection()],
    #histFileName=output_analysis+f"/histo_{label_name}.root",
    #histDirName="Events",
    provenance = True,
    noOut = False,
    maxEntries = 10000
)



p_vars.run()





