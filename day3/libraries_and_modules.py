#Libraries and Modules

#Python has very extensive libraries and modules, this is great for DevOps engineers!

#Libraries = COLLECTION of modules. Needs to be installed with pip.

#Modules = SINGLE file of functions, classes, variables etc. That you can bring in and use in another
#python file

import math
import random
import requests


num_float = 23.3

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)

rand_list = [1,2,3,4,5,6,7]
print(random.choice(rand_list))

rand_num = random.randint(1,10)
print(rand_num)

request_bbc = requests.get("https://www.bbc.co.uk/")

print(request_bbc.content)

bbc_content = request_bbc.content
print(type(bbc_content))

request_poke = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

print(request_poke.status_code)
print(request_poke.content)

poke_content = request_poke.content