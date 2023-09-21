#Scripting

# There are seven modules that we can consider "core" in python

import sys
import os
import subprocess
import math
import random
import datetime
import json

# sys

# print(sys.version)
#

# # os
# print(os.getcwd())
# os.chdir()

#subprocess

subprocess.run(["python","hello_world.py"])

#math

pi = math.pi
pi_string = str(pi)

#random

random_num = random.randrange(1,10)
print(random_num)

#date time

date = datetime.datetime.now()
print(date)

#json

x = {
    "name":"John",
    "age":30,
    "city":"london"
}

print(type(x))

y = json.dumps(x)
print(type(y))

print(y)