

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

# 获取第3个<li>标签, 不能用属性精确定位
result3 = selector.xpath('//li[1]').getall()

print(result3)

"""
    xpath语法中(用的非常多)
        对于获取到的多个统计标签, 可以用 [] 精确定位到你想取的第几个
        [] 内部天统计标签排列的顺序位置, 类似索引取值, 索引从1开始
        
    []
        可以用于通过属性精确定位
        可以用于同级标签的取值
"""



