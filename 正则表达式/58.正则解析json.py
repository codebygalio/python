"""
1. 采集网址 https://haokan.baidu.com/tab/gaoxiao_new

2. 采集目标
	- 采集当前页面里面的数据
	- 需要需要采集以下数据:
		title 视频标题
		duration 视频时长
		fmplaycnt 播放量

    - 用正则表达式采集
"""
import re

import requests


# 请求地址
url = 'https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=20&shuaxin_id=1650887667693'

# 发送请求
response = requests.get(url=url)
json_data = response.json()
# print(json_data)  # -- 对象


"""
{'id': '8065636952978692217', 'title': '(.*?)', 'poster_small': 'https://f7.baidu.com/it/u=1989216745,3607126174&fm=222&app=108&f=JPEG@s_0,w_660,h_370,q_80', 'poster_big': 'https://f7.baidu.com/it/u=1989216745,3607126174&fm=222&app=108&f=JPEG@s_0,w_660,h_370,q_80', 'poster_pc': 'https://f7.baidu.com/it/u=1989216745,3607126174&fm=222&app=108&f=JPEG@s_0,w_660,h_370,q_80', 'source_name': '农村吴妹', 'play_url': 'http://vd3.bdstatic.com/mda-ndhi7b0x29v6en1f/cae_h264_delogo/1650287783371020407/mda-ndhi7b0x29v6en1f.mp4?v_from_s=hkapp-haokan-nanjing', 'duration': '(.*?)', 'url': 'https://haokan.hao123.com/v?vid=8065636952978692217&pd=pc&context=', 'show_tag': 0, 'publish_time': '6天前', 'is_pay_column': 0, 'like': '21', 'comment': '0', 'playcnt': '2989', 'fmplaycnt': '(.*?)', 'fmplaycnt_2': '2989', 'outstand_tag': '', 'previewUrlHttp': 'https://vd3.bdstatic.com/mda-ndhi7b0x29v6en1f/cae_h264_delogo/1650287783371020407/mda-ndhi7b0x29v6en1f.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1650889975-0-0-7f61d4f2f90140f06636ac0233547903&bcevod_channel=searchbox_feed&pd=1&vt=1&cd=0&watermark=0&did=&logid=0175094457&vid=8065636952978692217&pt=0&appver=&model=&cr=0&abtest=peav_l52&sle=1&sl=482&split=521505', 'third_id': '1715552860960785', 'vip': 0, 'author_avatar': 'https://pic.rmb.bdstatic.com/bjh/user/66080e20b7cb6e7267f1fab51fc2c9af.jpeg?x-bce-process=image/resize,m_lfit,w_200,h_200&autime=19485'}
{.*?, 'title': '(.*?)', .*?'duration': '(.*?)',.*?'fmplaycnt': '(.*?)',.*?}
\{.*?, 'title': '(.*?)', .*?'duration': '(.*?)',.*?'fmplaycnt': '(.*?)',.*?\}
"""
json_str = str(json_data)
print(json_str)

result = re.findall("\{.*?, 'title': '(.*?)', .*?'duration': '(.*?)',.*?'fmplaycnt': '(.*?)',.*?\}", json_str, re.S)
print(result)

