"""

workspage=ext={"authorId":"j2deP_BZ_iqfxkUl6Y4aIQ","authorType":"ugc"}&refresh_state=2&pgext={"refresh_time":1603869526,"list_min_time":16034437804824}

workspage=ext%3D%257B%2522authorId%2522%253A%2522j2deP_BZ_iqfxkUl6Y4aIQ%2522%252C%2522authorType%2522%253A%2522ugc%2522%257D%26refresh_state%3D2%26pgext%3D%257B%2522refresh_time%2522%253A1603869526%252C%2522list_min_time%2522%253A16034437804824%257D
workspage=ext%3D%257B%2522authorId%2522%253A%2522j2deP_BZ_iqfxkUl6Y4aIQ%2522%252C%2522authorType%2522%253A%2522ugc%2522%257D%26refresh_state%3D2%26pgext%3D%257B%2522refresh_time%2522%253A1603869526%252C%2522list_min_time%2522%253A16034437804824%257D

"""
import urllib.parse

data1 = '{"authorId":"j2deP_BZ_iqfxkUl6Y4aIQ","authorType":"ugc"}'
data2 = '{"refresh_time":1603869526,"list_min_time":16034437804824}'

data3 = '=' + urllib.parse.quote(data1) + '&refresh_state=2&pgext=' + urllib.parse.quote(data2)
data4 = 'workspage=ext' + urllib.parse.quote(data3)
# print('workspage=ext'
#       + urllib.parse.quote('=')
#       + urllib.parse.quote(urllib.parse.quote(data1))
#       + urllib.parse.quote('&refresh_state=2&pgext=')
#       + urllib.parse.quote(urllib.parse.quote(data2))
#       )
print(data4)
