# 把字体文件读取为python能理解的对象
from fontTools.ttLib import TTFont

# 字体文件名字
font_name = 'SFoISQft.woff'

base_font = TTFont(font_name)
# 将字体关系保存为 xml 格式
base_font.saveXML('font.xml')
# 获取映射规则
map_list = base_font.getBestCmap()
# 字符编码：字符内容
print(map_list)

# 需要把英文转化为中文
# 映射规则是不变了
eng_2_num = {
    'period': ".", 'two': '2', 'zero': '0', 'five': '5', 'nine': "9", 'seven': '7', 'one': '1', 'three': '3',
    'six': '6', 'four': '4', 'eight': '8'
}

for key in map_list.keys():
    map_list[key] = eng_2_num[map_list[key]]
print(map_list)