#!/bin/tcsh 

#setenv X509_USER_PROXY /uscms/home/dburns7/x509up_u48626
#source /uscmst1/prod/sw/cms/setup/cshrc prod
#setenv SCRAM_ARCH slc5_amd64_gcc462
#pushd /uscms_data/d1/dburns7/CrabWorkingArea/CMSSW_5_3_11/src
#pushd /uscms_data/d1/dburns7/CrabWorkingArea/CMSSW_5_3_11_patch6/src
#cmsenv
#popd
#SSC
#DS
unset CMS_PATH
source /share/apps/cmssoft/cmsset_default.sh
pushd /home/dburns/WorkingArea/gentest/CMSSW_5_3_11/src
cmsenv
popd

echo "$X509_USER_PROXY"

#lcg-ls --verbose -b -D srmv2 "srm://cmssrm.fnal.gov:8443/srm/managerv2?SFN=/11/store/user/dburns7/test2.txt"

set JOB=1000
set EVTS=99900
set INFILE=file:ggTOhTOzzTO4l_8TeV.lhe
set OUTFILE=final_PAT_$JOB.root
set maxEvents=1

#echo "$EVTS"
#echo "Processing events "$EVTS" to $(($EVTS+$maxEvents)) in $INFILE. Outputting to $OUTFILE."

cmsDriver.py Configuration/Generator/python/Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff.py -s GEN,SIM --eventcontent RAWSIM --datatier GEN-SIM --mc --conditions auto:mc --filein=$INFILE --fileout=step1.root -n $maxEvents --no_exec

sed -i "/    fileNames = cms.untracked.vstring('$INFILE')/a \ \ \ \ , skipEvents = cms.untracked.uint32($EVTS)" Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff_py_GEN_SIM.py

cmsRun Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff_py_GEN_SIM.py

cmsDriver.py REDIGI -s DIGI,L1,DIGI2RAW,HLT:@relval --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions auto:mc -n $maxEvents --filein=file:step1.root --fileout=step2.root --pileup 2012_Summer_50ns_PoissonOOTPU

cmsDriver.py RECO --step RAW2DIGI,L1Reco,RECO --conditions auto:mc -n $maxEvents --filein=file:step2.root --fileout=step3.root --eventcontent RECOSIM --datatier GEN-SIM-RECO --pileup 2012_Summer_50ns_PoissonOOTPU

cmsRun simple_PAT_MC_cfg.py inputFiles=file:step3.root outputFile=$OUTFILE













#!/bin/tcsh
#setenv pwd $PWD
#echo ${1}
#cp /tmp/x509up_u45743 /uscms/home/dokstolp/
####Complie now
#g++ -Wno-deprecated myPlot.C -o myPlot_${1}.exe -I$ROOTSYS/include -L$ROOTSYS/lib `root-config --cflags` `root-config --libs`
#cat>Job_DM_${1}.csh<<EOF
##!/bin/tcsh
#setenv X509_USER_PROXY /uscms/home/dokstolp/x509up_u45743
#source /uscmst1/prod/sw/cms/setup/cshrc prod
#setenv SCRAM_ARCH slc5_amd64_gcc462
#cd /uscms_data/d3/dokstolp/monoHiggs/DM/CMSSW_5_3_11_patch6/src 
#cmsenv
#eval `scramv1 runtime -csh`
#cd ${pwd}
##SSC
#DS
#echo ${CMSSW_SEARCH_PATH}
#ls
#cmsRun config_DM_AxialVector_m5_${1}.py
#/opt/d-cache/srm/bin/srmcp "file://localhost/nuTuple_SUSY_${1}.root" "srm://cmssrm.fnal.gov:8443/11/store/user/dokstolp/DM_lowEt/nuTuple_SUSY_${1}.root"
#EOF
#

