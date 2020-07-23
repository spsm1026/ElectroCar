import requests
from bs4 import BeautifulSoup

search_keyword = '전기자동차'
url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_keyword}'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
news_titles = soup.select('.news .type01 li dt a[title]')

print('총', len(news_titles), '개의 뉴스 제목이 있습니다')
print()
for title in news_titles:
    print(title['title'])
     


