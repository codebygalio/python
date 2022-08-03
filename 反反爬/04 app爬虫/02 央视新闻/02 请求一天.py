"""
GET http://api.cportal.cctv.com/api/rest/articleInfo/getScrollList?n=20&version=1&p=1&pubDate=1546325473000&app_version=808 HTTP/1.1
User-Agent: SEA-AL10
X-Tingyun-Id: 85B-vX9WltU;c=2;r=1153749375;u=4c7f9966daf8d1746d1b20adda8461876c506415b5c4ce30950533d4383517fb::D9C566710A373F18
Host: api.cportal.cctv.com
Connection: Keep-Alive
Accept-Encoding: gzip

GET http://api.cportal.cctv.com/api/rest/articleInfo/getScrollList?n=20&version=1&p=2&pubDate=1546325473000&app_version=808 HTTP/1.1
User-Agent: SEA-AL10
X-Tingyun-Id: 85B-vX9WltU;c=2;r=118235680;u=4c7f9966daf8d1746d1b20adda8461876c506415b5c4ce30950533d4383517fb::D9C566710A373F18
Host: api.cportal.cctv.com
Connection: Keep-Alive
Accept-Encoding: gzip

GET http://api.cportal.cctv.com/api/rest/articleInfo/getScrollList?n=20&version=1&p=3&pubDate=1546325473000&app_version=808 HTTP/1.1
User-Agent: SEA-AL10
X-Tingyun-Id: 85B-vX9WltU;c=2;r=1754166269;u=4c7f9966daf8d1746d1b20adda8461876c506415b5c4ce30950533d4383517fb::D9C566710A373F18
Host: api.cportal.cctv.com
Connection: Keep-Alive
Accept-Encoding: gzip

"""
import requests
import pprint
day_url = 'http://api.cportal.cctv.com/api/rest/articleInfo/getScrollList'

"""
n=20&version=1&p=1&pubDate=1546325473000&app_version=808
n=20&version=1&p=2&pubDate=1546325473000&app_version=808
n=20&version=1&p=3&pubDate=1546325473000&app_version=808
"""

headers = {
    "User-Agent": "SEA-AL10",
    "X-Tingyun-Id": "85B-vX9WltU;c=2;r=1153749375;u=4c7f9966daf8d1746d1b20adda8461876c506415b5c4ce30950533d4383517fb::D9C566710A373F18",
    "Host": "api.cportal.cctv.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
}

recode_total = 20

while True:
    params = {
        "n": "20",
        "version": "1",
        "p": f'{int(recode_total/20)}',
        "pubDate": "1546325473000",
        "app_version": "808",
    }
    print(params)
    response = requests.get(day_url, params=params, headers=headers)
    data = response.json()
    for item in data['itemList']:
        # pprint.pprint(item)
        print('itemID', item['itemID'])
        # print('detailUrl', item['detailUrl'])
        print('itemTitle', item['itemTitle'])
        # print('operate_time', item['operate_time'])
        # print('pubDate', item['pubDate'])
        print('---------------------------')

    if recode_total < data['total']:
        recode_total += 20
    else:
        break
