"""
    目标网址: http://www.zfcg.sh.gov.cn
            1. 点击页面导航栏中 "采购公告" 栏目
            2. 采集下面公告信息数据, 需要采集以下数据:
                title  公告标题
                url    公告详情页地址
                districtName 公告区域
            3. 采集完后打印输出
"""
import requests

url = 'http://www.zfcg.sh.gov.cn/front/search/category'

json_data = {
    "utm": "sites_group_front.2ef5001f.0.0.277cfba0c0a211ec967dcb4c12e9aa96",
    "categoryCode": "ZcyAnnouncement3012",
    "pageSize": '15',
    "pageNo": '1'
}

response = requests.post(url=url, json=json_data)
json_data_str = response.json()
print(json_data_str)

# 数据解析
data_list = json_data_str['hits']['hits']

for da in data_list:
    title = da['_source']['title']
    url = da['_source']['url']
    districtName = da['_source']['districtName']
    print(title, url, districtName)
