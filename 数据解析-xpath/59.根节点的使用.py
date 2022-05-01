

html_str = """
        <div> 
            <ul> 
                <li class="item-1">
                    <a href="link1.html">第一个</a>
                </li> 
                
                <li class="item-2">
                    <a href="link2.html">第二个</a>
                </li> 
                
                <li class="item-3">
                    <a href="link3.html">第三个</a>
                </li> 
                
                <li class="item-4">
                    <a href="link4.html">第四个</a>
                </li> 
                
                <li class="item-5">
                    <a href="link5.html">第五个</a> 
                </li>
            </ul>
        </div>
"""

import parsel  # 内置xpath解析的方法


# 1.转换数据类型
# 在转换类型的时候, 能够把缺失的标签自动补全
selector = parsel.Selector(html_str)
# print(selector)

# 2.解析数据
# 从根节点开始, 获取所有的 <a> 标签
result = selector.xpath('/html/body/div/ul/li/a').getall()
print(result)

"""
    xpath语法中
    /   表示从根节点开始提取, 还表示取下一级标签, 用的极少
    如果打算从根节点提取, 所有html数据的根节点都是<html>标签
"""



