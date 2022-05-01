"""
逆向推导:
    1. 抓包获取到音频真实播放地址
    2. 根据音频地址找地址来源, 找到在某个数据包返回的内容里面有音频播放地址
    3. 分析第2步数据请求, 知道地址中id参数是请求所有音频的关键
    4. 分析id是哪里来的?  在当前的静态网页中有id值

代码逻辑:
    1. 在当前的静态网页中解析所有的id
    2. 根据id的变换请求json数据, 解析返回的音频地址
    3. 请求音频地址保存
"""

import requests
import parsel


# 1. 找数据对应的地址
url = 'https://www.ximalaya.com/youshengshu/2684034/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)  # 在数据解析之前, 一定要打印看数据是不是获取到了

# with open('a.html', mode='w', encoding='utf-8') as f:
#     f.write(html_data)


# 3.数据解析
selector = parsel.Selector(html_data)
lis = selector.css('.sound-list.Lp_>ul>li')
# print(lis)

for li in lis:
    title = li.css('.title.Mi_::text').get()  # 标题
    href_data = li.css('.text.Mi_>a::attr(href)').get()
    # print(title, href_data)
    m4a_id = href_data.split('/')[-1]
    # print(title, m4a_id)

    # 根据id的变换请求json数据, 解析返回的音频地址
    m4a_id_response = requests.get(url=f'https://www.ximalaya.com/revision/play/v1/audio?id={m4a_id}&ptype=1', headers=headers)
    data_json = m4a_id_response.json()
    m4a_url = data_json['data']['src']  # 解析到的音频地址
    # print(m4a_url)

    # 请求音频数据
    m4a_data = requests.get(url=m4a_url).content
    file_name = title + '.m4a'
    # print(file_name)

    with open('video\\' + file_name, mode='wb') as file:
        file.write(m4a_data)
        print('保存完成:', file_name)

