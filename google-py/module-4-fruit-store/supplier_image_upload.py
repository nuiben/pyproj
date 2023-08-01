#!/usr/bin/env python3

import os, requests
site = "http://localhost/upload/"

for jpeg in os.listdir(image_directory):
    if img.endswith('.jpeg'):
        print('processing...' + jpeg)
        image_path = image_directory + image_name
        with open(image_path, 'rb') as image:
            request = requests.post(site, files={'file': image})
