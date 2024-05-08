#==============================================================================
# BASELINE MACHINE LEARNING MODEL TO COMPARE TO OTHER ML MODELS
#==============================================================================
# Importing required libraries
import os
import sys
import pandas as pd
import json

#------------------------------------------------------------------------------
# Define target directories

paths_arg = sys.argv[1]

with open(paths_arg) as json_paths: 
    PATHS = json.load(json_paths)
    json_paths.close()

extracted_path = PATHS['extracted_data_path']

#------------------------------------------------------------------------------
# Read in data

csv_file = sys.argv[2]
data = pd.read_csv(extracted_path + csv_file)

#------------------------------------------------------------------------------
# 








#------------------------------------------------------------------------------

print("Hello World")