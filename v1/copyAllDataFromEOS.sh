#!/bin/bash

eval `scramv1 runtime -sh`
for sample in SingleMu_Run2012A
  do
  for iJob in `seq 0 7`
    do
    for MTBin in high low
      do
       #cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v1/muHadAnalysis_${MTBin}MT_${sample}_${iJob}_v1.root /mnt/hadoop/store/user/kmtos/data1/kmtos/data/analysis/ #BLINDED!!!
       #rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v1/muHadAnalysis_${MTBin}MT_${sample}_${iJob}_v1.root #BLINDED!!!
done
    done
done

exit 0
