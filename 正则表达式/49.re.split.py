import re



"""
split  分割字符串
pattern    正则匹配
string     需要匹配的数据
maxsplit   指定最大分割次数
"""
string = 'hjPython 123 ahsdgjasgh 456 Pythonasdjajsk'

result = re.split('\d+', string, maxsplit=1)
print(result)


