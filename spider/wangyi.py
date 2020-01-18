# 确定url
# import requests
# url = 'https://m10.music.126.net/20200118002209/64bdcd502a719987a7403825cfa3d3d1/yyaac/515f/515e/0153/f5b27e7a44f45ccc688a69fc281cfdde.m4a'
# base_url = 'https://link.hhtjim.com/163/1476106.mp3'
# result = requests.get(url).content
# with open('./hhh.m4a','wb') as f:
#     f.write(result)
# 确定url地址
# 导入库
import re
ul = re.findall(r'<ul class="f-hide">.*?</ul>', result, re.S)[0]
song_list = re.findall(r'id=(.*?)">(.*?)</a></li>',ul)
for song_info in song_list:
    song_id,song_name = song_info
    print(song_name)
    print(song_id)
    song_url = base_url + '%s' % song_id + '.mp3'
    print(song_url)

music = requests.get(song_url).content
with open('./music/%s.m4a'%song_name,'wb') as f:
f.write(music)