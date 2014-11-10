#!/bin/bash

eval `scramv1 runtime -sh`
for sample in `seq 1 1`
  do
  #for cut in Iso NonIso NonIsoReweight
  for cut in Iso NonIso
    do
    for MTBin in high low
      do
      if [ "$cut" != "NonIso" ] || [ 0 -eq 0 ]
          then
          cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHad${cut}Analysis_${MTBin}MT_WW_v2.root /mnt/hadoop/store/user/kmtos/data1/kmtos/WW/analysis/
          rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/v2/muHad${cut}Analysis_${MTBin}MT_WW_v2.root
      fi
    done
  done
done

exit 0