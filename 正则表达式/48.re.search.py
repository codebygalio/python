import re

string = 'hjPythonahsdgjasghPythonasdjajsk'

# re.search() 从字符串的任意位置匹配内容,
# 只能匹配一次
# 返回的是对象, 可以用 group() 取值
result = re.search('Python', string)
print(result.group())
