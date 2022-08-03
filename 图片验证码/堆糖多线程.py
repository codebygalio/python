"""
	目标网址：https://www.duitang.com/

	作业描述：请在网页最上面搜索框输入关键字 “蜡笔小新” 进行搜索图片，根据搜索到的结果采集前十页图片

	作业要求：用多进程嵌套多线程的方式实现
"""
import requests
import concurrent.futures


def send_requests(url):
    """发送请求"""
    response = requests.get(url=url)
    return response

def parse_data(data):
    """数据解析"""
    data_list = data['data']['object_list']

    img_url_list = []  # 接受所有的图片地址
    for data_l in data_list:
        img_url = data_l['photo']['path']  # 图片地址
        img_url_list.append(img_url)

    return img_url_list

def save_data(file_name, data):
    with open('img\\' + file_name, mode='wb') as f:
        f.write(data)
        print('保存完成: ', file_name)

def save_one_img(img_url):
    """定义一个保存一张图片的函数"""
    img_data = send_requests(img_url).content  # 图片数据
    file_name = img_url.split('/')[-1]  # 图片名字
    save_data(file_name, img_data)

def main(url):
    json_data = send_requests(url).json()
    imgUrl_list = parse_data(json_data)
    print(imgUrl_list)

    """将每一张图片任务分发给多线程"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for imgUrl in imgUrl_list:
            executor.submit(save_one_img, imgUrl)

if __name__ == '__main__':
    # main('https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%96%B0&after_id=72&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1652701984156')

    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as exec:
        for i in range(10):
            url = f'https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%96%B0&after_id={i * 24}&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1652701984156'
            exec.submit(main, url)