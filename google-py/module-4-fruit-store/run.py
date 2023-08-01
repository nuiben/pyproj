#!/usr/bin/env python3

import os, requests, json

site = 'http://localhost/fruits/'
path = ('./supplier-data/descriptions/')


for filename in os.listdir(path):
        with open(path + filename, "r") as f:
            lines = f.read().splitlines()
            content = dict(zip(("name","weight","description"), lines))
            temp = content['weight'].split(" ")
            if temp[0].isnumeric():
                content['weight'] = int(temp[0])
            content['image_name'] = filename[:-4]+".jpeg"
            response = requests.post(site, json=content)
            response.raise_for_status()
            response.close()
