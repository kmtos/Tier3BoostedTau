#!/bin/bash

if [ $# -gt 3 ]
    then
    echo "Usage: ./generateWJetsToLNuTauAnalyzerCfgs.sh <version> <template cfg> [reweightOnly]"
    exit 0
fi

####STUFF TO CONFIGURE####

#version
version=$1
templateCfg=$2
infoTag=""
reweightOnly=0
if [ "$3" == "reweightOnly" ]
    then
    reweightOnly=1
fi
dir=$version

#number of samples
nSamples=1
iBeg=0
iEnd=`expr $nSamples - 1`

#input file prefix
inputFilePrefix="file:/mnt/hadoop/store/user/kmtos/NMSSM_Files/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball-Summer12_DR53X-PU_S10_START53_V7A-v1-AODSIM_skim_v3/"

#CleanJets output file prefix
#cleanJetsOutputFilePrefix="`pwd`/${dir}/"
cleanJetsOutputFilePrefix="file:/`pwd`/${dir}/"

#TauAnalyzer output file prefix
#tauAnalyzerOutputFilePrefix="/data1/yohay/WZ/analysis/"
tauAnalyzerOutputFilePrefix="file:/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHad_files/"

#EDM output file prefix
EDMOutputFilePrefix="file:/mnt/hadoop/store/user/kmtos/data1/`whoami`/WJetsToLNu/EDM_files/"

####VECTORS OF QUANTITIES FOR EACH SAMPLE####

#vector of input file blocks for each sample
inputFileBlocks=( "readFiles.extend([\n    '${inputFilePrefix}data_no_selection_10_1_SwY.root',\n    '${inputFilePrefix}data_no_selection_11_1_S7l.root',\n    '${inputFilePrefix}data_no_selection_12_1_chj.root',\n    '${inputFilePrefix}data_no_selection_13_1_Z3I.root',\n    '${inputFilePrefix}data_no_selection_14_1_9z3.root',\n    '${inputFilePrefix}data_no_selection_15_1_tJo.root',\n    '${inputFilePrefix}data_no_selection_16_1_lqt.root',\n    '${inputFilePrefix}data_no_selection_17_1_s1O.root',\n    '${inputFilePrefix}data_no_selection_18_1_Y6w.root',\n    '${inputFilePrefix}data_no_selection_19_1_uPV.root',\n    '${inputFilePrefix}data_no_selection_1_1_jcU.root',\n    '${inputFilePrefix}data_no_selection_20_1_vXY.root',\n    '${inputFilePrefix}data_no_selection_21_1_gUn.root',\n    '${inputFilePrefix}data_no_selection_22_1_ecK.root',\n    '${inputFilePrefix}data_no_selection_23_1_STE.root',\n    '${inputFilePrefix}data_no_selection_24_1_Am2.root',\n    '${inputFilePrefix}data_no_selection_25_1_fIc.root',\n    '${inputFilePrefix}data_no_selection_26_1_yXz.root',\n    '${inputFilePrefix}data_no_selection_27_1_Aiw.root',\n    '${inputFilePrefix}data_no_selection_28_1_UGx.root',\n    '${inputFilePrefix}data_no_selection_29_1_bao.root',\n    '${inputFilePrefix}data_no_selection_2_1_dMr.root',\n    '${inputFilePrefix}data_no_selection_30_1_nDv.root',\n    '${inputFilePrefix}data_no_selection_31_1_yoq.root',\n    '${inputFilePrefix}data_no_selection_32_1_QPG.root',\n    '${inputFilePrefix}data_no_selection_33_1_3UD.root',\n    '${inputFilePrefix}data_no_selection_34_1_LJ9.root',\n    '${inputFilePrefix}data_no_selection_35_1_evM.root',\n    '${inputFilePrefix}data_no_selection_36_1_uW5.root',\n    '${inputFilePrefix}data_no_selection_37_1_dtn.root',\n    '${inputFilePrefix}data_no_selection_38_1_jzk.root',\n    '${inputFilePrefix}data_no_selection_39_1_Pma.root',\n    '${inputFilePrefix}data_no_selection_3_1_HT6.root',\n    '${inputFilePrefix}data_no_selection_40_1_oN7.root',\n    '${inputFilePrefix}data_no_selection_41_1_3ra.root',\n    '${inputFilePrefix}data_no_selection_4_1_9On.root',\n    '${inputFilePrefix}data_no_selection_5_1_U6A.root',\n    '${inputFilePrefix}data_no_selection_6_1_DMg.root',\n    '${inputFilePrefix}data_no_selection_7_1_IJL.root',\n    '${inputFilePrefix}data_no_selection_8_1_FUW.root',\n    '${inputFilePrefix}data_no_selection_9_1_3y5.root'\n    ])" )

#CleanJets output file
cleanJetsOutFiles=( "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_WJetsToLNu.root" )

#TauAnalyzer output files
isoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_WJetsToLNu_${version}.root" )
nonIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_WJetsToLNu_${version}.root" )
nonIsoReweightTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoReweightAnalysis_WJetsToLNu_${version}.root" )
allTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadAnalysis_WJetsToLNu_${version}.root" )

#EDM output files
EDMOutputFiles=( "${EDMOutputFilePrefix}WJetsToLNu${infoTag}_${version}.root" )

#samples
samples=( "WJetsToLNu" )

####GENERATION LOOP####

#change to working directory
mkdir -p $dir
cd $dir

#loop over number of samples
for i in `seq $iBeg $iEnd`
  do

  #generate cfg file for the isolated sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%NONISOTAUANALYZEROUTFILE%${nonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%ALLTAUANALYZEROUTFILE%${allTauAnalyzerOutputFiles[${i}]}%" -e "s%ISOTAUANALYZEROUTFILE%${isoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%SEQUENCE%process.isoTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%REWEIGHT%False%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_iso_cfg.py

  #generate cfg file for the non-isolated sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%NONISOTAUANALYZEROUTFILE%${nonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%ALLTAUANALYZEROUTFILE%${allTauAnalyzerOutputFiles[${i}]}%" -e "s%ISOTAUANALYZEROUTFILE%${isoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%SEQUENCE%process.nonIsoTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%REWEIGHT%False%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_nonIso_cfg.py

  #generate cfg file for the non-isolated, reweighted sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%NONISOTAUANALYZEROUTFILE%${nonIsoReweightTauAnalyzerOutputFiles[${i}]}%" -e "s%ALLTAUANALYZEROUTFILE%${allTauAnalyzerOutputFiles[${i}]}%" -e "s%ISOTAUANALYZEROUTFILE%${isoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%SEQUENCE%process.nonIsoTauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%REWEIGHT%True%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_nonIsoReweight_cfg.py

  #generate cfg file for the sample with no isolation cut
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%NONISOTAUANALYZEROUTFILE%${nonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%ALLTAUANALYZEROUTFILE%${allTauAnalyzerOutputFiles[${i}]}%" -e "s%ISOTAUANALYZEROUTFILE%${isoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%SEQUENCE%process.tauAnalysisSequence%" -e "s%PUSCENARIO%S10%" -e "s%REWEIGHT%False%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_all_cfg.py

  #generate iso+nonIso+reweight job submission script for LSF
  cat <<EOF > tauanalyzer_${samples[${i}]}_cfg.sh
#!/bin/bash
echo "Running tauanalyzer_${samples[${i}]}_cfg.sh"
jobDir="`pwd`"
fileNamePrefix="tauanalyzer_${samples[${i}]}"

cd \$jobDir
eval \`scramv1 runtime -sh\`
cd -
cmsenv
cp \$jobDir/\${fileNamePrefix}_iso_cfg.py \$jobDir/\${fileNamePrefix}_nonIso_cfg.py \$jobDir/\${fileNamePrefix}_nonIsoReweight_cfg.py .
echo "First copy done"
cmsRun \${fileNamePrefix}_iso_cfg.py > cmsRun_\${fileNamePrefix}_iso_cfg.out
echo "cmsRun \${fileNamePrefix}_iso_cfg.py DONE"
if [ $reweightOnly -eq 0 ]
    then
    cmsRun \${fileNamePrefix}_nonIso_cfg.py > cmsRun_\${fileNamePrefix}_nonIso_cfg.out
    echo "cmsRun \${fileNamePrefix}_nonIso_cfg.py DONE"
    echo "List of files to be copied in nonIsoTauAnalyzerOutputFiles in if statement: "
    ls -1 ${nonIsoTauAnalyzerOutputFiles[${i}]}
    cp -f ${nonIsoTauAnalyzerOutputFiles[${i}]} /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/
    rm ${nonIsoTauAnalyzerOutputFiles[${i}]}
    echo "Just copied to \$work and removed the files within the if statement"
fi
echo "End of if statement"
cmsRun \${fileNamePrefix}_nonIsoReweight_cfg.py > cmsRun_\${fileNamePrefix}_nonIsoReweight_cfg.out
echo "cmsRun \${fileNamePrefix}_nonIsoReweight_cfg.py DONE"
echo "List of files to be copied in isoTauAnalyzerOutputFiles: "
ls -1 ${isoTauAnalyzerOutputFiles[${i}]}
cp -f ${isoTauAnalyzerOutputFiles[${i}]} /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/
echo "List of files to be copied in nonIsoReweightTauAnalyzerOutputFiles: "
ls -1 ${nonIsoReweightTauAnalyzerOutputFiles[${i}]}
cp -f ${nonIsoReweightTauAnalyzerOutputFiles[${i}]} /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/
rm ${isoTauAnalyzerOutputFiles[${i}]} ${nonIsoReweightTauAnalyzerOutputFiles[${i}]} 

exit 0
EOF
  chmod a+x tauanalyzer_${samples[${i}]}_cfg.sh

  #generate noIsoCut job submission script for LSF
  #NOTE: the "echo" and "ls" commands in this CAT are all Kyle Tos's adding to figure out what is wrong with Condor running this program
  cat <<EOF > tauanalyzer_${samples[${i}]}_all_cfg.sh
#!/bin/bash
echo "Running tauanalyzer_${samples[${i}]}_all_cfg.sh"
jobDir="`pwd`"
fileNamePrefix="tauanalyzer_${samples[${i}]}"

cd \$jobDir
eval \`scramv1 runtime -sh\`
cd -
cp \$jobDir/\${fileNamePrefix}_all_cfg.py .
echo "First copy DONE"
cmsenv
cmsRun \${fileNamePrefix}_all_cfg.py > cmsRun_\${fileNamePrefix}_all_cfg.out
echo "cmsRun \${fileNamePrefix}_all_cfg.py DONE"
echo "List of the files in {allTauAnalyzerOutputFiles[${i}]} to be copied: "
ls -1 ${allTauAnalyzerOutputFiles[${i}]}
cp -f ${allTauAnalyzerOutputFiles[${i}]} /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/
rm ${allTauAnalyzerOutputFiles[${i}]}
echo "Removing DONE and file execution DONE"

exit 0
EOF
  chmod a+x tauanalyzer_${samples[${i}]}_all_cfg.sh
done

#generate run cfg that runs all files in the directory
cat <<EOF > runWJetsToLNuTauAnalyzerCfgs.sh
#!/bin/bash
cmsenv

for file in \`ls -alh *WJetsToLNu*.py | awk '{ print \$9 }'\`
  do
  outFile=\`echo \$file | sed -e "s%\.py%.txt%"\`
  cmsRun \$file > \$outFile
done

exit 0
EOF
chmod a+x runWJetsToLNuTauAnalyzerCfgs.sh

#generate script that submits all iso+nonIso+reweight jobs to LSF
cat <<EOF > submitWJetsToLNuTauAnalyzerJobs.sh
#!/bin/bash

for file in \`ls -alh tauanalyzer*WJetsToLNu*.sh | grep -v all | awk '{ print \$9 }'\`
  do
  jobName=\`echo \$file | sed -e "s%\(.*\)\.sh%\1%"\`
  echo "\$file"

  cat>Csubmit_\$jobName<<EOF
Universe   = vanilla
Executable = \$file
Log        = Csubmit_\$jobName.log
Output     = Csubmit_\$jobName.out
Queue
EOF

echo "EOF

echo \"generateWJetsToLNuTauAnalyzerCfgs.sh\"
condor_submit  Csubmit_\$jobName
done
exit 0" >> submitWJetsToLNuTauAnalyzerJobs.sh
chmod a+x submitWJetsToLNuTauAnalyzerJobs.sh

#generate script that submits all noIsoCut jobs to LSF
cat <<EOF > submitWJetsToLNuAllTauAnalyzerJobs.sh
#!/bin/bash

for file in \`ls -alh tauanalyzer*WJetsToLNu*all*.sh | awk '{ print \$9 }'\`
  do
  jobName=\`echo \$file | sed -e "s%\(.*\)\.sh%\1%"\`
  echo "\$file"

  cat>Csubmit_\$jobName<<EOF
Universe   = vanilla
Executable = \$file
Log        = Csubmit_\$jobName.log
Output     = Csubmit_\$jobName.out
Queue
EOF

echo "EOF

echo \"generateWJetsToLNuTauAnalyzerCfgs.sh\"
condor_submit  Csubmit_\$jobName
done
exit 0" >> submitWJetsToLNuTauAnalyzerJobs.sh
chmod a+x submitWJetsToLNuAllTauAnalyzerJobs.sh

#generate script that copies all iso+nonIso+reweight files locally from EOS
cat <<EOF > copyWJetsToLNuFromEOS.sh
#!/bin/bash

eval \`scramv1 runtime -sh\`
for sample in \`seq `expr $iBeg + 1` `expr $iEnd + 1`\`
  do
  for cut in Iso NonIso NonIsoReweight
    do
    if [ "\$cut" != "NonIso" ] || [ $reweightOnly -eq 0 ]
        then
        cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHad\${cut}Analysis_WJetsToLNu_${version}.root /mnt/hadoop/store/user/kmtos/data1/`whoami`/WJetsToLNu/analysis/
        rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHad\${cut}Analysis_WJetsToLNu_${version}.root
    fi
  done
done

exit 0
EOF
chmod a+x copyWJetsToLNuFromEOS.sh

#generate script that copies all noIsoCut files locally from EOS
cat <<EOF > copyAllWJetsToLNuFromEOS.sh
#!/bin/bash

eval \`scramv1 runtime -sh\`
for sample in \`seq `expr $iBeg + 1` `expr $iEnd + 1`\`
  do
  cp -f /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHadAnalysis_WJetsToLNu_${version}.root /mnt/hadoop/store/user/kmtos/data1/`whoami`/WJetsToLNu/analysis/
  rm /home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/muHadAnalysis_WJetsToLNu_${version}.root
done

exit 0
EOF
chmod a+x copyAllWJetsToLNuFromEOS.sh

exit 0
