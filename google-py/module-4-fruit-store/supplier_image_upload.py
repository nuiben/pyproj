#!/usr/bin/env python3

import os, requests
image_directory = "./supplier-data/images/"
site = "http://localhost/upload/"

for jpeg in os.listdir(image_directory):
    if jpeg.endswith('.jpeg'):
        print('processing...' + jpeg)
        image_path = image_directory + jpeg
        with open(image_path, 'rb') as image:
            request = requests.post(site, files={'file': image})
