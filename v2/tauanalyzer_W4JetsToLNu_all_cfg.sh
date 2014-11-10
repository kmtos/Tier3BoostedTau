#!/bin/bash
echo "Running tauanalyzer_W4JetsToLNu_all_cfg.sh"
jobDir="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2"
fileNamePrefix="tauanalyzer_W4JetsToLNu"

eval `scramv1 runtime -sh`
cmsRun ${fileNamePrefix}_all_cfg.py
echo "cmsRun ${fileNamePrefix}_all_cfg.py DONE"
exit 0
