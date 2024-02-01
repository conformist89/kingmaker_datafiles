import os
import yaml
import json 
import argparse

parser = argparse.ArgumentParser(
    description="produce dataset.yaml file for KingMaker"
)
parser.add_argument("--era", required=True, type=str, help="Experiment era.")
args = parser.parse_args()

root_folder = "/work/olavoryk/king_maker_setup/booseted_setup/KingMaker/sample_database/"+args.era+"/"

filelist = [

"dyjets/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",
"dyjets/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",
"dyjets/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml", 


"diboson/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv12-106X.yaml",
# "diboson/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv12-106X.yaml",
"diboson/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv12-106X.yaml",
"diboson/ZZTo4L_TuneCP5_13TeV_powheg_pythia8_RunIISummer20UL18NanoAODv12-106X.yaml",

"singletop/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",
"singletop/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",
"singletop/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",
"singletop/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",

"ttbar/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",
"ttbar/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",
"ttbar/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",

"wjets/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",
"wjets/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16NanoAODv12-106X.yaml",
    
"data/SingleMuon_Run2016F-UL2016.yaml",
"data/SingleMuon_Run2016G-UL2016.yaml",
"data/SingleMuon_Run2016H-UL2016.yaml",

]


my_top_new_json  = {}


for file in filelist:
    filename = root_folder+file
    
    with open(filename) as f:
        data = yaml.safe_load(f)

        my_json = {}
        my_json["dbs"] = data["dbs"]
        my_json["era"] = data["era"]
        my_json["generator_weight"] = data["generator_weight"]
        my_json["nevents"] = data["nevents"]
        my_json["nfiles"] = data["nfiles"]
        my_json["nick"] = data["nick"]
        my_json["sample_type"] = data["sample_type"]
        my_json["xsec"] = data["xsec"]

        my_new_json  = {}   
        my_new_json[data["nick"]] = my_json

        my_top_new_json[data["nick"]] = my_json


my_top_new_json
with open('/work/olavoryk/king_maker_setup/booseted_setup/KingMaker/sample_database/datasets.yaml', 'w') as fout:
    yaml.dump(my_top_new_json, fout, default_flow_style=False)