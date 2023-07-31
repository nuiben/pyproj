#! /usr/bin/env python3

import os
import requests

path = '/data/feedback/'

for file_name in os.listdir(path):
    print('--------------')
    print('FILE : ' + file_name)
    with open(path + file_name, 'r') as file:
        data = file.read().split('\n')
        print(data)
        user_review = {'title' : data[0], 'name' : data[1], 'date' : data[2], 'feedback' : data[3]}
        user_feedback = requests.post('http://<external_link>/feedback/', json = user_review)
    print('--------------')
    print(user_feedback.status_code)
