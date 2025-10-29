import os
import optparse
import sys
import time
from sample import *
from get_file_fromdas_F import *
import argparse

parser = argparse.ArgumentParser(description="Submitter on Condor")


parser.add_argument("-fh","--folder_histo",type =str, required = True, help = "Folder_path_for_histo")
parser.add_argument("-fr","--folder_root",type = str, required = True, help = "Folder_path_for_root_skim_file")

options = parser.parse_args()

folder_histo_count = options.folder_histo
folder_root_skim = options.folder_root




"""
usage = 'python submit_condor.py -d dataset_name -f destination_folder'
parser = optparse.OptionParser(usage)
parser.add_option('-d', '--dat', dest='dat', type=str, default = '', help='Please enter a dataset name')
parser.add_option('-f', '--folder', dest='folder', type=str, default = '', help='Please enter a destination folder')
#parser.add_option('-u', '--user', dest='us', type='string', default = 'ade', help="")
(opt, args) = parser.parse_args()
#Insert here your uid... you can see it typing echo $uid
"""




username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
if username == 'adeiorio':
    uid = 103214
elif username == 'acagnott':
    uid = 140541
elif username == "fconfort":
    uid = 179351


def sub_writer(path, dat_name, outname, label, folder_histo_count, folder_root_skim, label_name):
    f = open("condor.sub", "w")
    f.write("Proxy_filename          = x509up\n")
    f.write("Proxy_path              = /afs/cern.ch/user/" + inituser + "/" + username + "/private/$(Proxy_filename)\n")
    f.write("universe                = vanilla\n")
    f.write("x509userproxy           = $(Proxy_path)\n")
    f.write("use_x509userproxy       = true\n")
    f.write("should_transfer_files   = YES\n")
    f.write("when_to_transfer_output = ON_EXIT\n")
    f.write("transfer_input_files    = $(Proxy_path)\n")
    #f.write("transfer_output_remaps  = \""+outname+"_Skim.root=root://eosuser.cern.ch///eos/user/"+inituser + "/" + username+"/DarkMatter/topcandidate_file/"+dat_name+"_Skim.root\"\n")
    f.write("+JobFlavour             = \"testmatch\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week
    f.write("executable              = runner.sh\n")
    f.write("arguments               = "+path+" "+dat_name+" "+outname+" "+label+" "+ folder_histo_count + " " + folder_root_skim + " " + label_name +"\n")
    #f.write("input                   = input.txt\n")
    f.write("output                  = condor/output/"+ label_name+".out\n")
    f.write("error                   = condor/error/"+ label_name+".err\n")
    f.write("log                     = condor/log/"+ label_name+".log\n")

    f.write("queue\n")

if not os.path.exists("condor/output"):
    os.makedirs("condor/output")
if not os.path.exists("condor/error"):
    os.makedirs("condor/error")
if not os.path.exists("condor/log"):
    os.makedirs("condor/log")
if(uid == 0):
    print("Please insert your uid")
    exit()
if not os.path.exists("/tmp/x509up_u" + str(uid)):
    os.system('voms-proxy-init --rfc --voms cms -valid 192:00')
os.popen("cp /tmp/x509up_u" + str(uid) + " /afs/cern.ch/user/" + inituser + "/" + username + "/private/x509up")


#Dataset cycles 


'''
datasets = ['tDM_mPhi1000_mChi1']#, 'QCD_HT1000','QCD-HT1500to2000_2018', 'QCD-HT2000toInf_2018', 
            #'TT_Mtt-700to1000_2018', 'TT_Mtt-1000toInf_2018', 'TT_SemiLep_2018', 'TT_Hadr_2018']
datasets= {
    #'tDM_mPhi1000_mChi1': '/eos/home-a/acagnott/DarkMatter/prepro/tDM_mPhi1000_mChi1.root',
    #'tDM_mPhi500_mChi1': '/eos/home-a/acagnott/DarkMatter/prepro/tDM_mPhi500_mChi1.root',
    #'tDM_mPhi50_mChi1': '/eos/home-a/acagnott/DarkMatter/prepro/tDM_mPhi50_mChi1.root',
    'QCD_HT200to300_2018': 'root://cms-xrd-global.cern.ch///store/mc/RunIIAutumn18NanoAODv7/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/130000/5096FFDA-A47E-1846-AE02-033E0F144FF6.root',
    #'QCD_HT300to500_2018': 'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18NanoAODv7/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/120000/41889A83-F0A0-2143-AFB2-8041D63D3141.root',
    #'QCD_HT500to700_2018': 'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18NanoAODv7/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/100000/D2F139EF-CB80-404D-955F-B8D8E682D682.root',
    'QCD_HT700to1000_2018': 'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18NanoAODv7/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/260000/EE305C43-E265-BB4A-B6FA-60B447464524.root',
}
'''
#datasets = QCD_2018.components+TT_2018.components+ZJetsToNuNu_2018.components+[TprimeToTZ_700_2018, TprimeToTZ_1000_2018, TprimeToTZ_1800_2018]
#datasets = [ZJetsToNuNu_HT800to12#00_2018]
#datasets = [TT_2024_semilep.components[0]]
#datasets = [TT_bar_2024.components[1]]


#datasets = [tWb_Signal_4FS.components[0]]
datasets = TT_bar_2024.components


#datasets = []

#datasets = [TT_bar_2024.components[0]]
#datasets = W_to_Jets.components
#datasets = tW.components
#datasets = [tW.components[3]]





"""
for d in datasets:
    dat = get_files_string(d)[1]
    dat = 'root://cms-xrd-global.cern.ch//'+dat
    outname=dat.split("/")[-1].replace('.root', '_Skim.root')
    final_name = '/eos/home-a/acagnott/DarkMatter/testfileskim/'+d.label+'_Skim.root'
    label = d.label
    sub_writer(dat, final_name, outname, label)
    print(d.label)
    print(dat)
    os.popen('condor_submit condor.sub')
    time.sleep(5)
"""





for d in datasets:
    files = get_files_string(d)   

    for i, f in enumerate(files):
        dat = 'root://cms-xrd-global.cern.ch//' + f

        if i >= 202:
        # nome output incrementale
            outname = f"{d.label}_{i}_Skim.root"
            final_name = f"/eos/f/fconfort/NanoAOD_outputs/{outname}"
            label = f"{d.label}"
            label_name = f"{d.label}_{i}"

            # scrive il file condor.sub
            sub_writer(dat, final_name, outname, label, folder_histo_count, folder_root_skim, label_name)

            print(f"Submitting job for {label_name}, file {i}")
            print(dat)

            os.popen('condor_submit condor.sub')
            time.sleep(3)

            if i == 700:
                break



