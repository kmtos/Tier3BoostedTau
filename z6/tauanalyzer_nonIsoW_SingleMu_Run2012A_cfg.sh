#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

echo "Running tauanalyzer_nonIsoW_SingleMu_Run2012A_cfg.sh"
jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/z6"
fileNamePrefix="tauanalyzer_nonIsoW_SingleMu_Run2012A"

eval `scramv1 runtime -sh`
cmsRun ${fileNamePrefix}_iso_cfg.py 
echo "cmsRun fileName_iso_cfg.py DONE"
if [ 0 -eq 0 ]
    then
    echo "Just inside first if loop"
    cmsRun ${fileNamePrefix}_nonIso_cfg.py 
fi
#cmsRun ${fileNamePrefix}_nonIsoReweight_cfg.py 
#echo "cmsRun ${fileNamePrefix}_nonIsoReweight_cfg.py DONE"
exit 0
