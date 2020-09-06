import json
import re
jsn_dict = {}
with open("jawiki-country.json") as fp:
    for jsn_fp in fp:
        jsn = json.loads(jsn_fp)
        jsn_dict[jsn["title"]] = jsn["text"]

pattern = re.compile(r"^(={2,})\s*(.+)\s*(={2,}).*$",re.MULTILINE)
matches = pattern.findall(jsn_dict["イギリス"])
for match in matches:
    print('  '*(len(match[0])-1), match[1].split("=")[0],len(match[0])-1) 

