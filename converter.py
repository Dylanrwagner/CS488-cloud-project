#Convert Data  from xml file to json file that can be imported into mongo
import xmltodict
import json

with open('dblp-data.xml') as fd:
    doc = xmltodict.parse(fd.read())

publications, people = {}, {}

for x in doc["PROX3DB"]["ATTRIBUTES"]["ATTRIBUTE"]:
    if x["@NAME"] == "object-type":
        for val in x["ATTR-VALUE"]:
            if val["COL-VALUE"] == "person":
                people.update({val["@ITEM-ID"] : []})
            else:
                publications.update({val["@ITEM-ID"] : {}})

    elif x["@NAME"] == "name":
        for val in x["ATTR-VALUE"]:
            people[val["@ITEM-ID"]].append(val["COL-VALUE"])
    elif x["@ITEM-TYPE"] == "O":
        for val in x["ATTR-VALUE"]:
            publications[val["@ITEM-ID"]].update({x["@NAME"] : val["COL-VALUE"]})

for x in doc["PROX3DB"]["LINKS"]["LINK"]:
    if x["@O1-ID"] in people:
        if "authors" in publications[x["@O2-ID"]]:
            publications[x["@O2-ID"]]["authors"].append({x["@O1-ID"] : people[x["@O1-ID"]]})  
        else:
            publications[x["@O2-ID"]].update({"authors" : [{x["@O1-ID"] : people[x["@O1-ID"]]}]})
    elif x["@O2-ID"] in people:
        if "authors" in publications[x["@O1-ID"]]:
            publications[x["@O1-ID"]]["authors"].append({x["@O2-ID"] : people[x["@O2-ID"]]})  
        else:
            publications[x["@O1-ID"]].update({"authors" : [{x["@O2-ID"] : people[x["@O2-ID"]]}]})

final_table = []
for k, v in publications.items():
    line = {"_id" : k}
    for keys, values in v.items():
        line.update({keys : values})
    final_table.append(line)
        
for row in final_table:
    print(json.dumps(row, separators=(', ', ': ')))
