import json
import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()

    else:
        print("Sorry... " + sys.argv[1] + "Not Found")
        exit(1)
else:
    print("Usage: json_to_yaml.py <source_file.json> [target_file.yaml]")

output = yaml.dump(source_content)

if len(sys.argv) < 3:
    print(output)

elif os.path.exists(sys.argv[2]):
    print("Sorry... " + sys.argv[2] + " Already Exists")
    exit(1)

else:
    target_file = open(sys.argv[2], "w")
    target_file.write(output)
    target_file.close()