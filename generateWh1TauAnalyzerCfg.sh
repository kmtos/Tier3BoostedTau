#!/bin/bash

if [ $# -ne 2 ]
    then
    echo "Usage: ./generateWh1TauAnalyzerCfg.sh <version> <template cfg>"
    exit 0
fi

####STUFF TO CONFIGURE####

#version
version=$1
templateCfg=$2
infoTag=""
dir=$version

#number of samples
nSamples=6
iBeg=0
iEnd=`expr $nSamples - 1`

#input file prefix
inputFilePrefix="file:/mnt/hadoop/store/user/kmtos/data1/kmtos/Wh1_Medium/EDM_files/"

#CleanJets output file prefix
cleanJetsOutputFilePrefix="`pwd`/${dir}/"
#cleanJetsOutputFilePrefix=""

#TauAnalyzer output file prefix
tauAnalyzerOutputFilePrefix="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/OUTPUT/Wh1/"
#tauAnalyzerOutputFilePrefix=""

#EDM output file prefix
EDMOutputFilePrefix="/home/kmtos/NMSSM_Analysis/CMSSW_5_3_11/src/BoostedTauAnalysis/TauAnalyzer/test/OUTPUT/Wh1/EDM/"

####VECTORS OF QUANTITIES FOR EACH SAMPLE####

#vector of input file blocks for each sample
inputFileBlocks=( "readFiles.extend([\n    '${inputFilePrefix}data_no_selection_a5_v6.root'\n    ])" "readFiles.extend([\n    '${inputFilePrefix}data_no_selection_a7_v6.root'\n    ])" "readFiles.extend([\n    '${inputFilePrefix}data_no_selection_a9_v6.root'\n    ])" "readFiles.extend([\n    '${inputFilePrefix}data_no_selection_a11_v6.root'\n    ])" "readFiles.extend([\n    '${inputFilePrefix}data_no_selection_a13_v6.root'\n    ])" "readFiles.extend([\n    '${inputFilePrefix}data_no_selection_a15_v6.root'\n    ])" )

#CleanJets output file
cleanJetsOutFiles=( "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_Wh1_a5.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_Wh1_a7.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_Wh1_a9.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_Wh1_a11.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_Wh1_a13.root" "${cleanJetsOutputFilePrefix}NMSSMSignal_MuProperties_Wh1_a15.root" )

#TauAnalyzer output files
highMTIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_highMT_Wh1_a5_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_highMT_Wh1_a7_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_highMT_Wh1_a9_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_highMT_Wh1_a11_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_highMT_Wh1_a13_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_highMT_Wh1_a15_${version}.root" )
lowMTIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_lowMT_Wh1_a5_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_lowMT_Wh1_a7_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_lowMT_Wh1_a9_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_lowMT_Wh1_a11_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_lowMT_Wh1_a13_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadIsoAnalysis_lowMT_Wh1_a15_${version}.root" )
highMTNonIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_highMT_Wh1_a5_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_highMT_Wh1_a7_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_highMT_Wh1_a9_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_highMT_Wh1_a11_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_highMT_Wh1_a13_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_highMT_Wh1_a15_${version}.root" )
lowMTNonIsoTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_lowMT_Wh1_a5_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_lowMT_Wh1_a7_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_lowMT_Wh1_a9_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_lowMT_Wh1_a11_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_lowMT_Wh1_a13_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadNonIsoAnalysis_lowMT_Wh1_a15_${version}.root" )
highMTAllTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadAnalysis_highMT_Wh1_a5_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_highMT_Wh1_a7_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_highMT_Wh1_a9_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_highMT_Wh1_a11_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_highMT_Wh1_a13_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_highMT_Wh1_a15_${version}.root" )
lowMTAllTauAnalyzerOutputFiles=( "${tauAnalyzerOutputFilePrefix}muHadAnalysis_lowMT_Wh1_a5_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_lowMT_Wh1_a7_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_lowMT_Wh1_a9_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_lowMT_Wh1_a11_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_lowMT_Wh1_a13_${version}.root" "${tauAnalyzerOutputFilePrefix}muHadAnalysis_lowMT_Wh1_a15_${version}.root" )

#EDM output files
EDMOutputFiles=( "${EDMOutputFilePrefix}Wh1_a5${infoTag}_${version}.root" "${EDMOutputFilePrefix}Wh1_a7${infoTag}_${version}.root" "${EDMOutputFilePrefix}Wh1_a9${infoTag}_${version}.root" "${EDMOutputFilePrefix}Wh1_a11${infoTag}_${version}.root" "${EDMOutputFilePrefix}Wh1_a13${infoTag}_${version}.root" "${EDMOutputFilePrefix}Wh1_a15${infoTag}_${version}.root" )

#samples
samples=( "Wh1_a5" "Wh1_a7" "Wh1_a9" "Wh1_a11" "Wh1_a13" "Wh1_a15" )

####GENERATION LOOP####

#change to working directory
mkdir -p $dir
cd $dir

#loop over number of samples
for i in `seq $iBeg $iEnd`
  do

  #generate cfg file for the isolated sample
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${highMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTIsoTauAnalysisSequence%" -e "s%LOWMTSEQUENCE%process.lowMTIsoTauAnalysisSequence%" -e "s%REWEIGHT%True%" -e "s%PUSCENARIO%S10%" -e "s%SAMPLE%${samples[${i}]}%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_iso_cfg.py

  #generate cfg file for the sample with no isolation cut
  sed -e "s%FILES%${inputFileBlocks[${i}]}%" -e "s%CLEANJETSOUTFILE%${cleanJetsOutFiles[${i}]}%" -e "s%HIGHMTNONISOTAUANALYZEROUTFILE%${highMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTALLTAUANALYZEROUTFILE%${highMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%HIGHMTISOTAUANALYZEROUTFILE%${highMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTNONISOTAUANALYZEROUTFILE%${lowMTNonIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTALLTAUANALYZEROUTFILE%${lowMTAllTauAnalyzerOutputFiles[${i}]}%" -e "s%LOWMTISOTAUANALYZEROUTFILE%${lowMTIsoTauAnalyzerOutputFiles[${i}]}%" -e "s%EDMOUTFILE%${EDMOutputFiles[${i}]}%" -e "s%HIGHMTSEQUENCE%process.highMTIsoTauAnalysisSequence%" -e "s%LOWMTSEQUENCE%process.lowMTIsoTauAnalysisSequence%" -e "s%REWEIGHT%True%" -e "s%PUSCENARIO%S10%" -e "s%SAMPLE%${samples[${i}]}%" ../${templateCfg} > tauanalyzer_${samples[${i}]}_all_cfg.py
done

#generate run cfg that runs all files in the directory
cat <<EOF > runWh1IsoTauAnalyzerCfgs.sh
#!/bin/bash

for file in \`ls -alh *Wh1_a*_iso*.py | grep -v MET | awk '{ print \$9 }'\`
  do
  outFile=\`echo \$file | sed -e "s%\.py%.txt%"\`
  echo "file=  $file"
  echo "Output file= $outFile"
  cmsRun \$file >& \$outFile &
done

exit 0
EOF
chmod a+x runWh1IsoTauAnalyzerCfgs.sh

exit 0
