#!/bin/bash

eval `scramv1 runtime -sh`
for sample in `seq 1 4`
  do
  for MTBin in high low
  do
  cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/z6/muHadAnalysis_${MTBin}MT_W${sample}JetsToLNu_z6.root /mnt/hadoop/store/user/kmtos/data1/kmtos/WNJetsToLNu/analysis/
  rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/z6/muHadAnalysis_${MTBin}MT_W${sample}JetsToLNu_z6.root
  done
done

exit 0
