#!/usr/bin/python

from ConstData import AreaCode
import json
import os
import requests
from tqdm import tqdm

if not os.path.exists("./images"):
    os.mkdir("./images")

def download_file(url,save_path=None):
    if not save_path:
        save_path = url[url.rfind('/')+1:]
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024*16
    t=tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(save_path, 'wb') as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    if total_size != 0 and t.n != total_size:
        print("download error")


for item in AreaCode:
    sales_data = json.load(open('sales-%s-%s.json'%(item[0],item[1])))
    os.chdir('./images')
    for content in sales_data['contents']:
        img_url = content['hero_banner_url']
        print(content['formal_name'])
        download_file(img_url)
    os.chdir('..')
