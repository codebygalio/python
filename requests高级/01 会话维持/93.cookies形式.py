import requests

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

data = {
    'from': 'zh',
    'to': 'en',
    'query': '早上好',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '282438.44151',
    'token': '7c9c2c6ba5c542702efe6479623b8f0c',
    'domain': 'common',
}

headers = {
    # 请求会验证cookies
    # cookies可以添加在请求头里面
    # 'Cookie': 'BIDUPSID=D26C29435949C22624426B7C5A1F52F3; PSTM=1648641081; BAIDUID=D26C29435949C2262B46863076C03868:FG=1; BDUSS=RDQ2R2Y1BIZ3pQbzNvMG0tbkVpbHV3RXN2MmpJNlpLdUt4ZXRjRklJM1JObjVpRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANGpVmLRqVZidG; BDUSS_BFESS=RDQ2R2Y1BIZ3pQbzNvMG0tbkVpbHV3RXN2MmpJNlpLdUt4ZXRjRklJM1JObjVpRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANGpVmLRqVZidG; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=110085_127969_174434_179350_184716_185638_188332_189755_191243_194085_194519_196426_196528_197241_197711_197955_198268_199177_199312_199582_201107_201193_201546_201707_202284_202652_203190_203310_203525_204031_204100_204261_204700_204711_204859_204915_205218_205240_205484_205568_206729_206815_207003_207022_207236_207471_207729_207895_208001_208055_208115_208225_208268_208270_208309_208313_208344_208494_208521_208686_208718_208721_208770_208790_209075_209115_209436_209459_209489_209520_209527_209568_209577_209578_209674_209847_209980_210071_210163_210300_210356_210484; H_PS_PSSID=35837_36175_31660_34812_35910_36167_34584_36122_35979_36126_35802_36234_26350_36100_36061; BA_HECTOR=81052405a0a08004kn1h5qqd40q; BAIDUID_BFESS=D26C29435949C2262B46863076C03868:FG=1; delPer=0; PSINO=7; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1650289062; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1650289062; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_NjJlOGE1NzQzMGRkMzc5YzcwYTRkNGZlYTkxZGZhZWI3MDUwNGNiZDM0MWRiNTRiNzNiMWVjNzE4MThiNzQ3ZDY0NDBkZDhkMDg5ZGMxNjJjZTI0NWE3ZjEwZDg0ZjcyZTQwM2Y3MmExZjgzMDc1NDczMzU1Njc2NzkxMWE4YzAzOTRkNDdhMjkzZmRhYWE4OGFjZjMyNGU5ZTY4ZDdmNWM3NzU2MjZlZmU5NmYxYWQ3N2MwNWU2MmI1YzU2YmZm',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

"""# 单独把cookies构建字典"""
# cookies = {
#     'Cookie': 'BIDUPSID=D26C29435949C22624426B7C5A1F52F3; PSTM=1648641081; BAIDUID=D26C29435949C2262B46863076C03868:FG=1; BDUSS=RDQ2R2Y1BIZ3pQbzNvMG0tbkVpbHV3RXN2MmpJNlpLdUt4ZXRjRklJM1JObjVpRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANGpVmLRqVZidG; BDUSS_BFESS=RDQ2R2Y1BIZ3pQbzNvMG0tbkVpbHV3RXN2MmpJNlpLdUt4ZXRjRklJM1JObjVpRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANGpVmLRqVZidG; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=110085_127969_174434_179350_184716_185638_188332_189755_191243_194085_194519_196426_196528_197241_197711_197955_198268_199177_199312_199582_201107_201193_201546_201707_202284_202652_203190_203310_203525_204031_204100_204261_204700_204711_204859_204915_205218_205240_205484_205568_206729_206815_207003_207022_207236_207471_207729_207895_208001_208055_208115_208225_208268_208270_208309_208313_208344_208494_208521_208686_208718_208721_208770_208790_209075_209115_209436_209459_209489_209520_209527_209568_209577_209578_209674_209847_209980_210071_210163_210300_210356_210484; H_PS_PSSID=35837_36175_31660_34812_35910_36167_34584_36122_35979_36126_35802_36234_26350_36100_36061; BA_HECTOR=81052405a0a08004kn1h5qqd40q; BAIDUID_BFESS=D26C29435949C2262B46863076C03868:FG=1; delPer=0; PSINO=7; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1650289062; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1650289062; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_NjJlOGE1NzQzMGRkMzc5YzcwYTRkNGZlYTkxZGZhZWI3MDUwNGNiZDM0MWRiNTRiNzNiMWVjNzE4MThiNzQ3ZDY0NDBkZDhkMDg5ZGMxNjJjZTI0NWE3ZjEwZDg0ZjcyZTQwM2Y3MmExZjgzMDc1NDczMzU1Njc2NzkxMWE4YzAzOTRkNDdhMjkzZmRhYWE4OGFjZjMyNGU5ZTY4ZDdmNWM3NzU2MjZlZmU5NmYxYWQ3N2MwNWU2MmI1YzU2YmZm',
# }
"""构建cookies片段"""
cookies = {
# 'BAIDUID':'D26C29435949C2262B46863076C03868:FG=1',
'BAIDUID_BFESS':'D26C29435949C2262B46863076C03868:FG=1',  # 此字段是服务器会校验的cookie片段
# 'BIDUPSID': 'D26C29435949C22624426B7C5A1F52F3',
# 'PSTM': '1648641081',
# 'BDUSS': 'RDQ2R2Y1BIZ3pQbzNvMG0tbkVpbHV3RXN2MmpJNlpLdUt4ZXRjRklJM1JObjVpRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANGpVmLRqVZidG',
# 'BDUSS_BFESS': 'RDQ2R2Y1BIZ3pQbzNvMG0tbkVpbHV3RXN2MmpJNlpLdUt4ZXRjRklJM1JObjVpRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANGpVmLRqVZidG',
# 'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
# 'H_WISE_SIDS': '110085_127969_174434_179350_184716_185638_188332_189755_191243_194085_194519_196426_196528_197241_197711_197955_198268_199177_199312_199582_201107_201193_201546_201707_202284_202652_203190_203310_203525_204031_204100_204261_204700_204711_204859_204915_205218_205240_205484_205568_206729_206815_207003_207022_207236_207471_207729_207895_208001_208055_208115_208225_208268_208270_208309_208313_208344_208494_208521_208686_208718_208721_208770_208790_209075_209115_209436_209459_209489_209520_209527_209568_209577_209578_209674_209847_209980_210071_210163_210300_210356_210484',
# 'H_PS_PSSID': '35837_36175_31660_34812_35910_36167_34584_36122_35979_36126_35802_36234_26350_36100_36061',
# 'BA_HECTOR': '81052405a0a08004kn1h5qqd40q',
# 'delPer': '0',
# 'PSINO': '7',
# 'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1650289062',
# 'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1650289062',
# 'REALTIME_TRANS_SWITCH': '1',
# 'FANYI_WORD_SWITCH': '1',
# 'HISTORY_SWITCH': '1',
# 'SOUND_SPD_SWITCH': '1',
# 'SOUND_PREFER_SWITCH': '1',
# 'ab_sr': '1.0.1_NjJlOGE1NzQzMGRkMzc5YzcwYTRkNGZlYTkxZGZhZWI3MDUwNGNiZDM0MWRiNTRiNzNiMWVjNzE4MThiNzQ3ZDY0NDBkZDhkMDg5ZGMxNjJjZTI0NWE3ZjEwZDg0ZjcyZTQwM2Y3MmExZjgzMDc1NDczMzU1Njc2NzkxMWE4YzAzOTRkNDdhMjkzZmRhYWE4OGFjZjMyNGU5ZTY4ZDdmNWM3NzU2MjZlZmU5NmYxYWQ3N2MwNWU2MmI1YzU2YmZm',
}

# cookies  指定cookies关键字参数
response = requests.post(url=url, data=data, cookies=cookies, headers=headers)
print(response.json())


"""
cookies 是用户身份字段的表示

假设cookies在请求的时候, 服务器会进行校验, 具体的校验哪一个片段的cookies

cookies片段的来源?
    服务器生成cookies: 在响应的过程中, 生成cookies , 查找 Set-Cookie
    浏览器生成: 一般服务器不会校验
    js生成:  JavaScript<计算机语言>  一般加密, js逆向  <查询参数加密, 请求参数加密, 请求头字段加密>
    
浏览器会帮助我们在一定时间内维持用户登陆的状态

requests模块发送的所有请求都是单次请求, 每次请求之间没有联系

"""


