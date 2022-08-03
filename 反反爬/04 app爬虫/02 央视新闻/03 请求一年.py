"""
1546325473000 2019-01-01 14:51:13
1546411873000 2019-01-02 14:51:13
1546498273000 2019-01-03 14:51:13
"""
import datetime

import requests


def time_chain():
    time_chain_list = []
    start_data = datetime.date(2019, 1, 1)
    start_time = datetime.time(14, 51, 13)
    date_time_now = datetime.datetime.combine(start_data, start_time)

    day = datetime.timedelta(days=1)

    for i in range(7):
        # print(date_time_now.strftime('%Y-%M-%d'), int(date_time_now.timestamp() * 1000))
        time_chain_list.append([int(date_time_now.timestamp() * 1000), date_time_now.strftime('%Y-%M-%d')])
        date_time_now += day

    return time_chain_list



def download_one_day(datetime_now, data):
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
            "p": f'{int(recode_total / 20)}',
            "pubDate": f"{datetime_now}",
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


for datetime_now, data in time_chain():
    print(datetime_now, data)
    download_one_day(datetime_now, data)

