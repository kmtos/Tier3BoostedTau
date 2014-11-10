#!/bin/bash

eval `scramv1 runtime -sh`
for sample in "_s" "bar_s" "_t" "bar_t"
  do
  for MTBin in high low
    do
    cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadAnalysis_${MTBin}MT_T${sample}-channel_v2.root /mnt/hadoop/store/user/kmtos/data1/kmtos/SingleTop/analysis/
    rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHadAnalysis_${MTBin}MT_T${sample}-channel_v2.root
  done
done

exit 0
