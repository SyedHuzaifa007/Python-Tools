import os
import glob
import csv
import json

for file in glob.glob('*.csv'):
    csv_file = os.path.splitext(file)[0]
    json_file = csv_file + '.json'

    with open(csv_file+'.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(json_file, 'w') as f:
        json.dump(rows, f)