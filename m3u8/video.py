"""
[课    题]： Python爬取网站视频，下载流媒体m3u8格式视频

[主讲老师]：青灯教育 - 自游   上课时间 20:05

[模块使用]：
    requests >>> pip install requests (数据请求 第三方模块)
    re # 正则表达式 去匹配提取数据
    json

[开发环境]：
    Python 3.8 解释器
    Pycharm 2021.2 版本  建议

win + R 输入cmd 输入安装命令 pip install 模块名 如果出现爆红 可能是因为 网络连接超时 切换国内镜像源
先听一下歌 等一下后面进来的同学, 20:05 正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信: python10010
---------------------------------------------------------------------------------------------------
听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要跟着敲代码, 先听懂思路, 课后找木子老师领取录播, 然后再写代码
    3. 不要进进出出, 早退不仅没有录播, 你还会思路中断
---------------------------------------------------------------------------------------------------
模块安装问题:
    - 如果安装python第三方模块:
        1. win + R 输入 cmd 点击确定, 输入安装命令 pip install 模块名 (pip install requests) 回车
        2. 在pycharm中点击Terminal(终端) 输入安装命令
    - 安装失败原因:
        - 失败一: pip 不是内部命令
            解决方法: 设置环境变量

        - 失败二: 出现大量报红 (read time out)
            解决方法: 因为是网络链接超时,  需要切换镜像源
                清华：https://pypi.tuna.tsinghua.edu.cn/simple
                阿里云：https://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：https://pypi.hustunique.com/
                山东理工大学：https://pypi.sdutlinux.org/
                豆瓣：https://pypi.douban.com/simple/
                例如：pip3 install -i https://pypi.doubanio.com/simple/ 模块名

        - 失败三: cmd里面显示已经安装过了, 或者安装成功了, 但是在pycharm里面还是无法导入
            解决方法: 可能安装了多个python版本 (anaconda 或者 python 安装一个即可) 卸载一个就好
                    或者你pycharm里面python解释器没有设置好
---------------------------------------------------------------------------------------------------
如何配置pycharm里面的python解释器?
    1. 选择file(文件) >>> setting(设置) >>> Project(项目) >>> python interpreter(python解释器)
    2. 点击齿轮, 选择add
    3. 添加python安装路径
---------------------------------------------------------------------------------------------------
pycharm如何安装插件?
    1. 选择file(文件) >>> setting(设置) >>> Plugins(插件)
    2. 点击 Marketplace  输入想要安装的插件名字 比如:翻译插件 输入 translation / 汉化插件 输入 Chinese
    3. 选择相应的插件点击 install(安装) 即可
    4. 安装成功之后 是会弹出 重启pycharm的选项 点击确定, 重启即可生效
---------------------------------------------------------------------------------------------------

零基础同学 0
有基础同学 1 (写过爬虫案例)

爬虫实现流程思路:
一. 数据来源分析
    1. 确定目标网站  >>> 爬取网址是什么 数据是什么
    2. 通过开发者工具进行抓包分析
        爬取视频
            1. 先看network下面 media(媒体文件包含视频数据或者音频数据)  [如果没有数据]
            2. 通过数据包数据慢慢分析
    如果说url里面包含 ts 后缀 >>> 视频片段 >>> m3u8视频格式 (有专门m3u8文件保存所有ts文件内容)

m3u8 就是把一个整体视频, 分割成很多视频小片段 一个片段只有几秒时间...
    (可以更好缓存, 你看多少,他就给加载多少, 减少服务器压力)

    通过上述分析可以知道 只需要获取m3u8文件, 可以获取所有ts视频片段.....

二. 代码实现步骤: 发送请求 获取数据 解析数据 保存数据
第一次请求
    1. 发送请求, 对于视频详情页页面发送请求 https://www.acfun.cn/v/ac34063499
    2. 获取数据, 获取网页源代码
    3. 解析数据, 提取我们想要数据内容 视频信息
第二次请求:
    4. 发送请求, 对于m3u8 url地址发送请求
    5. 获取数据, 获取返回ts文件内容
    6. 解析数据, 提取所有ts文件

    保存数据, 把视频内容保存本地, 把视频片段合成为一个完整视频

lis = [1,2,3,5,4,6,7]
如果我想要提取lis这个列表里面 元素 1 怎么取 lis[0]  >>> 0 对应索引的位置

就业找工作 1
兴趣爱好 2
兼职赚钱小钱 3

可以加清风老师微信: pythonmiss
    1. 可以了解学习方向 以及 就业方向 (根据你们自身情况 定制学习内容)
    2. 可以免费领取 学习路线图 课程大纲
    3. 想要跟着老师付费学习, 想要老师手把手亲自教学 找清风了解, 可以领取优惠 学费减免 优惠活动


全套课程 核心编程 高级开发 爬虫实战 数据分析 全炸开发前端 全栈开发后端 学完7个月时间

直接面向就业找工作...8-15K左右薪资工作 程序员入门薪资
爬虫采集数据 >>> 制定课程大纲, 采集各大招聘平台关于python招聘需求数据, + 老师多年开经验 总结出来一套详细系列课程内容

按时听课, 按时完成作业, 老师可以就保证你可以学会掌握, 学会掌握之后 就就业找工作...

VIP付费课程授课方式:
    - 在线直播授课 每周 135 或者 246 晚上20:00-22:00
    - 课后会提供高清录播回放(永久观看学习) 源码 课件 笔记 软件工具 ....
    - 老师辅导解答 通过微信文字 语音 远程操作等方式解答辅导  鄙人...凌晨三点都可以解答辅导 (上午不行)
    - 提供重修, 如果你跟着老师学完一期课程之后,觉得直接学的不够扎实,是可以继续免费在跟着老师学习一期
        每节课都会提供作业的, 每个阶段都是考核的
    - 打电话通知听课
    - 提供就业指导
    - 提供外包 直接提供渠道 提供外包接单群...
    - 第三方平台(腾讯课堂)支付学费
    - 发票
    - 合同
    ....

课程学费 7880, 现在报名优惠后的学费 7180.... 并且还享有两年学习权限,  还会提供外包接单全, 渠道...
申请分期免息学习


金融 量化分析 爬虫+数据分析+金融专业知识
会计 自动化办公 批量处理数据 财务报表可视化展示
电商 爬虫 数据分析 采集商品数据 做客户人群分析 商品分析
Java 爬虫+数据分析+Java >>> 大数据开发
微信小程序 后端功能 flask框架 前端
游戏开发 pygame
脚本...


自学和系统区别
    1. 时间成本
        自学学多久?
            1-2年更甚至更久
        系统学7个月

    2. 学习资料时效性
        自学 各种平台 找学习资料 不一定最新的, 不一定是你能用的

        系统学习, 老师总结经验 最新教材 课程会实时更新

    3. 遇到问题怎么解决?
        自学 百度 谷歌 360 bing csdn 等等 方式 搜索你想要答案 不一定能够解决 解决时间会比较长

        系统学习 >> 专业的老师 直接远程操作辅导解答 5-10分钟左右 只要你问题描述的清楚 时间可以更短


自学一个月python, 然后发现自己学的python2


这个月有事情 没办法上课, 直接找班主任 冻结学习时间, 说明你情况, 之后有时间再来学都是可以的
    - 你报名之后所有老师都会给你进行服务 课程录播资料你都拥有

学员报名, 不是服务终止, 是服务的开始


我差的不是7000多的学费

    自学时间
        1-2年 还不一定能坚持学这么久 能够学的会
        24个月

    - 中间差距 17*10 = 17W
    - 还有3个月可以开始接外包 1000一个月计算  9*1000 = 9K
    系统学习7个月 10K薪资

程序员薪资 不跳槽 10%-20% 每年涨幅
    跳槽 50%-100%涨薪幅度

报名的同学  在学习的过程中遇到不懂的地方一定要多问老师, 不要觉得不好意思
有什么事情也可以和任何一位老师反馈...
"""
# 导入数据请求模块
import requests  # 第三方模块 pip install requests
# 导入正则
import re   # 内置模块 不需要安装
# 导入json
import json     # 内置模块 不需要安装
# 导入格式化输出模块
import pprint    # 内置模块 不需要安装


for page in range(8, 17):
    # 获取一页视频ID
    url = 'https://www.acfun.cn/u/45321802'
    data = {
        'quickViewId': 'ac-space-video-list',
        'reqID': '1',
        'ajaxpipe': '1',
        'type': 'video',
        'order': 'newest',
        'page': page,
        'pageSize': '20',
        't': '1648129818743',
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }
    response_1 = requests.get(url=url, params=data, headers=headers)
    video_ids = re.findall('ac(\d+)', response_1.text)
    for video_id in video_ids:
        """
        1. 发送请求, 对于视频详情页页面发送请求 https://www.acfun.cn/v/ac34063499
            I. 确定请求网址
            II. 确定请求方式
            III. 如何实现伪装 如何防止被反爬 user-agent: 用户代理 表示浏览器基本身份信息
                在开发者工具里面直接复制
        等号左边都是自定义变量 (见名知意)
        """
        url = f'https://www.acfun.cn/v/ac{video_id}'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
        }
        # 通过requests这个模块里面get请求方式, 对于url地址发送请求, 并且携带上headers请求头, 最后用自定义变量response接收返回数据
        response = requests.get(url=url, headers=headers)  # <Response [200]>  表示对象 200状态码表示请求成功
        # 2. 获取数据, 获取网页源代码 response.text 获取响应文本数据(字符串数据)
        # print(response.text)
        """
        3. 解析数据, 提取我们想要数据内容 视频信息
            正则表达式 可以直接对于字符串数据进行提取解析
        re.findall() 找到所有, 找数据 >>> 找什么样数据, 从哪里找数据
        防止有一种情况, 我们想要数据中间, 突然出现一个分号
        css 根据标签属性内容提取数据
        xpath 根据标签节点提取数据
        re 直接提取字符串数据
        """
        html_data = re.findall('window.pageInfo = window.videoInfo = (.*)', response.text)[0].replace(';', '')
        json_data = json.loads(html_data)
        # print(json_data)
        # pprint.pprint(json_data)
        # json_data 字典数据类型, 就可以根据键值对取值 根据冒号左边的内容(键) 提取冒号右边的内容(值)
        title = json_data['title']  # 提取视频标题
        m3u8_url = json.loads(json_data['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['backupUrl'][0]
        m3u8_data = requests.get(url=m3u8_url, headers=headers).text
        # print(m3u8_data)
        m3u8_data = re.sub('#E.*', '', m3u8_data).split()  # split() 字符串分割 返回列表数据
        for ts in m3u8_data:
            ts_url = '/'.join(m3u8_url.split('/')[:-1]) + '/' + ts
            print(ts_url)
            # ts_url = 'https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/' + ts
            # ts_url_1 = 'https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/' + ts
            # https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/
            ts_content = requests.get(url=ts_url, headers=headers).content
            # ab 以二进制数据追加保存不会覆盖 wb 二进制数据保存 会覆盖
            with open(title + '.mp4', mode='ab') as f:  # as
                f.write(ts_content)
        print(title, '视频保存成功', url)



