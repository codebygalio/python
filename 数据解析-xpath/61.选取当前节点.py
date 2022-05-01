

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

# 首先选中 <ul> 标签, 然后提取 <ul> 下所有的<li>标签
result = selector.xpath('//ul')
result2 = result.xpath('.//li').getall()


print(result2)

"""
    xpath语法中(用的非常多)
    .    表示取当前节点
    使用场景: 需要对选取的标签进行二次提取的时候, 需要用到 . 
"""



