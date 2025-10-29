#!/usr/bin/bash
cd /afs/cern.ch/user/f/fconfort/CMSSW_14_1_0/src/PhysicsTools/NanoAODTools/python/postprocessing/
cmsenv
export XRD_NETWORKSTACK=IPv4
python3 run_postproccesor.py $1 $2 $3 $4 $5 $6 $7
