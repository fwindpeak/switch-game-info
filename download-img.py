#!/usr/bin/python

from ConstData import AreaCode
import json
import os

if not os.path.exists("./images"):
    os.mkdir("./images")

for item in AreaCode:
    sales_data = json.load(open('sales-%s-%s.json'%(item[0],item[1])))
    os.chdir('./images')
    for content in sales_data['contents']:
        img_url = content['hero_banner_url']
        os.system('wget '+img_url)
    os.chdir('..')
