"""
将上课的案例-爬取小说完善。爬取《剑来》前面十章的小说数据,分别保存在不同的txt文件下

	-- 网址： https://www.bige7.com/book/1031/

请下下方开始编写代码
"""
import requests
import re
import os


def down_load(url, times=2):  # times 可以控制异常重试的次数, 如果超过两次任然会报错
                              # 默认会有一次请求 + 2次异常重试请求 = 3次
    """保存一个章节的逻辑"""
    try:
        response_2 = requests.get(url, timeout=0.4)
        data = response_2.text

        title = re.findall('<h1 class="wap_none">(.*?)</h1>', data, re.S)[0]

        result_contend = re.findall('<div id="chaptercontent" class=".*?">(.*?)</p></div>', data, re.S)
        contend = result_contend[0].replace('<br /><br />', '\n')

        with open('剑来\\' + title, mode='w', encoding='utf-8') as f:
            print('正在保存:', title)
            f.write(contend)
    except Exception as e:
        print(e)
        if times >= 1:
            # 函数的递归
            down_load(url, times - 1)  # 进行异常重试, 就减次数

if __name__ == '__main__':

    response = requests.get('https://www.bige7.com/book/1031/')
    html = response.text

    result_list = re.findall('<dd><a href ="(.*?)">.*?</a></dd>', html, re.S)
    if not os.path.exists('剑来'):  # 如果没有 剑来 文件夹在此项目路径中
        os.mkdir('剑来')

    for result in result_list:
        all_url = 'https://www.bige7.com' + result
        down_load(all_url)



