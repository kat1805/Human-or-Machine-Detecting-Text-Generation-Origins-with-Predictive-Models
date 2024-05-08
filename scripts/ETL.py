#==============================================================================
# EXTRACTING AND LOADING DATA FROM JSON FILES TO DATAFRAME
#==============================================================================
# Importing required libraries
import os
import sys
import json
import pandas as pd

#------------------------------------------------------------------------------
# Define target directories

paths_arg = sys.argv[1]

with open(paths_arg) as json_paths: 
    PATHS = json.load(json_paths)
    json_paths.close()

raw_path = PATHS['raw_data_path']
extracted_path = PATHS['extracted_data_path']

#------------------------------------------------------------------------------
# Extract raw json files

# Domain 1 human data
f = open(raw_path + 'set1_human.json')
d1_human_json = json.load(f)
f.close()

# Domain 1 machine data
f = open(raw_path + 'set1_machine.json')
d1_machine_json = json.load(f)
f.close()

# Domain 2 human data
f = open(raw_path + 'set2_human.json')
d2_human_json = json.load(f)
f.close()

# Domain 2 machine data
f = open(raw_path + 'set2_machine.json')
d2_machine_json = json.load(f)
f.close()

# Test data
f = open(raw_path + 'test.json')
test_json = json.load(f)
f.close()

#------------------------------------------------------------------------------
# Convert json files to dataframes

d1_human = pd.json_normalize(d1_human_json)
d1_machine = pd.json_normalize(d1_machine_json)
d2_human = pd.json_normalize(d2_human_json)
d2_machine = pd.json_normalize(d2_machine_json)
test = pd.json_normalize(test_json)

#------------------------------------------------------------------------------
# Adding machine_id for human datasets for mergeability (machine_id = 5)

d1_human['machine_id'] = 5
d2_human['machine_id'] = 5

#------------------------------------------------------------------------------
# Adding label to datasets

d1_human['label'] = 1
d2_human['label'] = 1
d1_machine['label'] = 0
d2_machine['label'] = 0

#------------------------------------------------------------------------------
# Merging human and machine data for domain 1 and domain 2

d1 = pd.concat([d1_human, d1_machine], ignore_index = True)
d2 = pd.concat([d2_human, d2_machine], ignore_index = True)

#------------------------------------------------------------------------------
# Save dataframes as csv files

d1.to_csv(extracted_path + 'd1.csv', index = False)
d2.to_csv(extracted_path + 'd2.csv', index = False)
test.to_csv(extracted_path + 'test.csv', index = False)

#------------------------------------------------------------------------------
print("Jsons have been converted to dataframes and saved to data/extracted")

