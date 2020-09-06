import json
jsn_dict = {}
with open("jawiki-country.json") as fp:
    for jsn_fp in fp:
        jsn = json.loads(jsn_fp)
        jsn_dict[jsn["title"]] = jsn["text"]
print(jsn_dict["イギリス"])