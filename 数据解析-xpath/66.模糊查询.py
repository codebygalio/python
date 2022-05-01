
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

# 了解模糊查询
result = selector.xpath('//li[contains(@class,"it")]').getall()
print(result)

"""
    xpath语法中
        contains(@class,"item") 表示模糊查询
        @class  模糊查询标签的属性名字
        item    模糊查询的关键走, 包含次关键字的标签都会被提取到

"""



