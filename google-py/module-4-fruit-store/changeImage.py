#!/usr/bin/env python3

import os, requests
site = "http://localhost/upload/"
path = "./supplier-data/images/"

for image in os.listdir(path):
    if image.endswith('.tiff'):
        print('processing...' + image)
        jpeg = Image.open(path+image)
        jpeg.convert('RGB').resize((600, 400)).save(path+image[:-5]+'.jpeg', "JPEG")
