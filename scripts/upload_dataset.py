# Standard imports
import os

# Project imports
import twinlab as tl

print()  #  Initial white space
directory = "datasets"
filename = "biscuits.csv"
dataset_id = filename
filepath = os.path.join(directory, filename)
tl.upload_dataset(filepath, dataset_id, verbose=True, debug=True)
