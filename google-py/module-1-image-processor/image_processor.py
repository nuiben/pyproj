#!/usr/bin/env python3

# Module 1 Project - Image Processor
# Developed using Python 3.11.4


# Using Pillow version 10.0.0
from PIL import Image
import os

img_path = './images/'
save_to_path = '/opt/icons/'

# Takes a string paramater, opens the matching file name using PIL.Image,
# rotates the image 90 degrees clockwise, resizing it to 128x128, and saves as a '.JPEG' to 'opt/icons/'
def flip_and_save(image_name):
    im = Image.open(img_path + image_name)
    im.rotate(-90).resize((128,128)).convert('RGB').save(save_to_path + image_name, "JPEG")

# Using the os module, the './images' directory is parsed, and file contents
# are stored in a list.
# A function call to flip_and_save passes the current file name for Image processing.
def main():
    files = [f for f in os.listdir(img_path)]
    for f in files:
        print('processing...' + f)
        flip_and_save(f)

if __name__ == '__main__':
    main()
