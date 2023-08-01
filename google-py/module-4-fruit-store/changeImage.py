#!/usr/bin/env python3

import os, requests
site = "http://localhost/upload/"
path = "./supplier-data/images/"

for jpeg in os.listdir(path):
    if jpeg.endswith('.jpeg'):
        print('processing...' + jpeg)
        with open(path+jpeg, 'rb') as image:
            request = requests.post(site, files={'file': image})
