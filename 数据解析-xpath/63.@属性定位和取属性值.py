

html_str = """
        <div> 
            <ul> 
                <li class="item-1">
                    <a href="link1.html">第一个</a>
                </li> 
                
                <li class="item-2", href="https://www.baidu.com/">
                    <a href="link2.html">第二个</a>
                </li> 
                
                <li class="item-3">
                    <a href="link3.html">第三个</a>
                </li> 
                
                <li class="item-4">
                    <a href="link4.html">第四个</a>
                </li> 
                
                <li class="item-5" >
                    <a href="link5.html" nihao="你好">第五个</a> 
                </li>
            </ul>
        </div>
"""

import parsel  # 内置xpath解析的方法


selector = parsel.Selector(html_str)

# 首先选中 <a> 标签的父节点, 取父节点的 class 属性
result = selector.xpath('//a')
result2 = result.xpath('../@href').getall()

# 获取第4个<a>标签,
result3 = selector.xpath('//a[@nihao="你好"]').getall()


print(result3)

"""
    xpath语法中(用的非常多)
    @   有两个用途
        1. 根据标签特有的属性, 获取其属性值
        2. 根据标签的属性, 做精确定位
        
        常见标签的属性 (class href src id title style)
"""



