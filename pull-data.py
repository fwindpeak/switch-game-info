import requests
from ConstData import AreaCode
import json

result = {}

for item in AreaCode:
    contents = []
    url_sales = "https://ec.nintendo.com/api/%s/%s/search/sales"%(item[0],item[1])
    count=30
    offset=0
    total = 0
    print(url_sales)
    while 1:
        r = requests.get('%s?count=%s&offset=%s'%(url_sales,count,offset)).json()
        contents += r['contents']
        total = r['total']
        print(total,offset)
        if offset+count >= total:
            break
        offset += count
    result = {
        'total':total,
        'contents':contents
    }
    json.dump(result,open('sales-%s-%s.json'%(item[0],item[1]),"w"))
