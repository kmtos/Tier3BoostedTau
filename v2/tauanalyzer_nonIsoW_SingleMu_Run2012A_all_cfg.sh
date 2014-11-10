#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

echo "Running tauanalyzer_nonIsoW_SingleMu_Run2012A_all_cfg.sh"
jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2"
fileNamePrefix="tauanalyzer_nonIsoW_SingleMu_Run2012A"

eval `scramv1 runtime -sh`
echo "First copy DONE"
cmsRun ${fileNamePrefix}_all_cfg.py 
echo "cmsRun ${fileNamePrefix}_all_cfg.py DONE"
exit 0
