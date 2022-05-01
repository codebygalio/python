import re


pattern = 'Java'
repl = 'Python'
string = 'Pythonasdkjasd Java adhuiaghsdk Java akjsdhkashdkja'

"""
pattern 正则语法
repl    正则匹配的数据需要替换的内容, (函数)  根据函数返回的内容进行替换
string  在哪里匹配替换
count   替换的次数
"""

# 15246895635
# 152****5635

def func(x):
    return 'Python'  # 函数的返回值就是最终替换的结果

result = re.sub(pattern, repl, string, count=1)
print(result)

result = re.sub(pattern, func, string)
print(result)
