#!/bin/bash
source /share/apps/cmssoft/cmsset_default.sh

echo "  Running tauanalyzer_SingleMu_Run2012C_6_all_cfg.sh"
jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v1"
fileNamePrefix="tauanalyzer_SingleMu_Run2012C_6"

eval `scramv1 runtime -sh`
echo "First copy DONE"
#cmsRun ${fileNamePrefix}_all_cfg.py  #BLINDED!!!
#echo "cmsRun ${fileNamePrefix}_all_cfg.py DONE"

exit 0
