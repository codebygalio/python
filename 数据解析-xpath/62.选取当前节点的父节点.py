

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


selector = parsel.Selector(html_str)

# 首先选中 <a> 标签的父节点,
result = selector.xpath('//a')
result2 = result.xpath('..').getall()


print(result2)

"""
    xpath语法中(用的非常多)
    ..    表示取当前节点的父节点(用的极少)
"""



