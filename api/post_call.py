#post requests to postcode api

import requests
import json

json_body = json.dumps({"postcodes" : ["ha01df","m45 6gn","ex165bl"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())