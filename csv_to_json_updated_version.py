import os
import glob
import csv
import json
from typing import Text

# Location of .csv files that we want to convert to json format
# Example: filePath = 'D:\Dev\Python\CSV_Files'
# filePath = '' means the current folder
filePath = ''; 

# file name with its extension (in this case the extension will be .csv)
# if we need to convert all .csv files of the above-mentioned folder then will use '*.csv' as file name
fileName = '*.csv'; 

# if no path is given then ignore path and use only the file name
# otherwise append file name with file path
if filePath == '':

    filePathAndName = fileName;

else:
    filePathAndName = filePath + '\\' + fileName;

# run a for loop that will cover all .csv files in the given / relevant folder
# one iteration of for loop will convert one .csv file into .json format
for file in glob.glob(filePathAndName):

    # get name of .csv file without its extension
    csv_file = os.path.splitext(file)[0]

    # create name for .json file by appending .json to the above mentioned file name
    json_file = csv_file + '.json'

    # read that .csv file and put all of its rows in the list "rows"
    with open(csv_file+'.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # dump all of those rows in the .json file
    with open(json_file, 'w') as f:
        json.dump(rows, f)