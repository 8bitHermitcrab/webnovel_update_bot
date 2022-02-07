import requests, time
from bs4 import BeautifulSoup

url = 'https://ncode.syosetu.com/n2267be/'
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

# URL과 헤더를 get으로 가져오기
res = requests.get(url, headers=headers)
# 오류 확인
res.raise_for_status()

# bs4로 페이지 분석
soup = BeautifulSoup(res.text, 'lxml')

# 현재 날짜와 시간
now_date = time.strftime('%Y/%m/%d %H:%M')
print(now_date)

# 업데이트 날짜와 시간 전부 가져오기
up_dates= soup.find_all('dt', attrs={'class' : 'long_update' })
# 날짜 부분만 전부 가져오기
for up_date in up_dates:
    ud = up_date.get_text()[0:12]
# 날짜 부분과 일치하면 링크 반환
if '2022/02/04' in ud:
# if now_date in ud:
    print('최신 업데이트가 있습니다. 페이지를 확인하세요 >> ', url)
else:
    print('최신 업데이트가 없습니다.')