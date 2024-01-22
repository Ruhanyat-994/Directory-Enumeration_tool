import os
import requests
import sys

file = f"{sys.argv[1]}"
path = os.getcwd() + file

dir_list = open(file).read()
directories= dir_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[2]}/{dir}.html"
    r = requests.get(dir_enum)
    if r.status_code != 404 :
         print("valid directory:",dir_enum)
       