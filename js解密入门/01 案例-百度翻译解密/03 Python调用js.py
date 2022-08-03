# 导入模块
import execjs  # 安装模块名:pyexecjs  导入的模块名: execjs


"""读取js代码"""
with open('02 百度翻译js.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

# 编译js代码
compile_result = execjs.compile(js_code)  # compile()  编译方法, 传递需要编译的js代码
print(compile_result)

# 调用
result = compile_result.call('e', '你好')
print(result)