#api requests
import json

import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/ha01df")

print(post_codes_req)
print(post_codes_req.headers) # gives the headers
print(post_codes_req.content)# gives json as bytes

post_codes_dict = json.loads(post_codes_req.content)
print(post_codes_dict)

print(post_codes_req.json())