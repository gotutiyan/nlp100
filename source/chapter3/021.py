import json
import re
jsn_dict = {}
with open("jawiki-country.json") as fp:
    for jsn_fp in fp:
        jsn = json.loads(jsn_fp)
        jsn_dict[jsn["title"]] = jsn["text"]

pattern = re.compile(r"^(.*\[\[Category:.*\]\].*)$", re.MULTILINE)
match = pattern.findall(jsn_dict["イギリス"])
print(match)