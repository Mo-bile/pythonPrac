import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 0) 출력 할 때는 `print(rank, title, artist)` 하면 됩니다!
#
# 1) 앞에서 두 글자만 끊기! `text[0:2]` 를 써보세요!
#
# 2) 순위와 곡제목이 깔끔하게 나오지 않을 거예요. 옆에 여백이 있다던가, 다른 글씨도 나온다던가.. 파이썬 내장 함수인 `strip()`을 잘 연구해보세요!
#
sample = soup.select_one('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)')
# print(sample.text)

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

for song in songs:
    rank = song.select_one('td.number').text[0:2].strip()
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    artist = song.select_one('td.info > a.artist.ellipsis').text

    # print(rank)
    # print(title)
    # print(artist)
    print(rank, title, artist)