import re

string = 'hjPythonahsdgjasghPythonasdjajsk'

# re.match() 从字符串的最开始的地方匹配内容, 如果需要匹配的字符串不在开始的地方, 就匹配不到
# 只能匹配一次
# 返回的是对象, 可以用 group() 取值
result = re.match('Python', string)
print(result)
