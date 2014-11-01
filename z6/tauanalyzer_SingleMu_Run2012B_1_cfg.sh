#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

echo "  Running tauanalyzer_SingleMu_Run2012B_1_cfg.sh"
jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/z6"
fileNamePrefix="tauanalyzer_SingleMu_Run2012B_1"

eval `scramv1 runtime -sh`
cmsRun ${fileNamePrefix}_iso_cfg.py  #BLINDED!!!
echo "cmsRun ${fileNamePrefix}_iso_cfg.py DONE"
if [ 0 -eq 0 ]
    then
    cmsRun ${fileNamePrefix}_nonIso_cfg.py 
    echo "cmsRun ${fileNamePrefix}_nonIso_cfg.py DONE"
fi
#cmsRun ${fileNamePrefix}_nonIsoReweight_cfg.py 
#echo "cmsRun ${fileNamePrefix}_nonIsoReweight_cfg.py DONE"

exit 0
