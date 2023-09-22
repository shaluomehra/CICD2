#Parsing is making something more understandable. So lets mke json more understandable for python
import json
#.loads takes the content from a json file and turn it into a python dictionary
parsed_json = json.loads(open("exampl_json.json").read())
print(parsed_json)
print(type(parsed_json))
value = parsed_json["name"]
print(value)
