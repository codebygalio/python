
"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458

    请用正则表达式实现:
"""

tel = "18123115458"

import re

def func(x):
    print('传进来匹配到的数据:', x)
    str_ = x.group()
    print(str_)

    return str_[:3] + '****' + str_[-4:]


# func 是 sub()  方法默认会调用的一个函数, 函数在传参的时候只传函数名
# 函数返回结果就是最终替换的结果
result = re.sub('\d{11,}', func, tel, re.S)
print(result)

result2 = re.sub('\d{11,}', lambda x:x.group()[:3] + '****' + x.group()[-4:], tel, re.S)
print(result2)


