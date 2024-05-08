#==============================================================================
# APPLY COUNT VECTORISATION TO TOKENS TO GATHER MEANINGFUL WORDS INFO
#==============================================================================
# Importing required libraries
import os
import sys
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer

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
# Generate new features using TF-IDF on text column

tfidf_vectorizer = TfidfVectorizer()
data_tfidf = tfidf_vectorizer.fit_transform(data['txt'])
vectorised_txt = pd.DataFrame(data_tfidf.toarray(),columns=tfidf_vectorizer.get_feature_names_out())

v_data = pd.concat([data, vectorised_txt], axis = 1)

#------------------------------------------------------------------------------
# Save dataframes as csv files

v_data.to_csv(extracted_path + csv_file[:-4] + "_v.csv", index = False)

#------------------------------------------------------------------------------

print(csv_file + " has been vectorised")

