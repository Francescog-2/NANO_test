import os, sys
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.tWb_Analysis.Histo_tWb import *


fnames = [sys.argv[1]]
final_name = sys.argv[2]
outname = sys.argv[3]
label = sys.argv[4]
folder_write_histo = sys.argv[5]



#os.makedirs("/eos/user/f/fconfort/NanoAOD_outputs/tWb_Analysis_Background_W_to_2Jets_Ele_histo", exist_ok=True)





p = PostProcessor(
    "/eos/user/f/fconfort/Prova", #
    fnames,         # lista di file da processare
    #cut=preselection,    # cut pretaglio
    branchsel=None,      # selezione dei branch (None prende tutti)
    modules=[Histo_tWb()],  # modulo che produce gli istogrammi tWb
    noOut=True,         # crea anche il file di output con gli eventi
    histFileName= "/eos/user/f/fconfort/NanoAOD_outputs/" + folder_write_histo+label+".root",
    #histFileName="histOut.root",
    histDirName="Events",                  
    provenance=True,
    #maxEntries=1000
)


p.run()

