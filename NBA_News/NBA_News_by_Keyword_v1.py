# coding: utf-8
from time import sleep

from bs4 import BeautifulSoup
import requests
import pandas

d_list = []
url = 'https://www.sportingnews.com/jp/nba/news/page/{}'

print('取得する記事の数を入力してください。\n')
n = int(input())

print('検索キーワードを入力してください。\nキーワードを設定しない場合は「NBA」と入力してください。\n')
keyword = input()

i = 1

while 1:
    target_url = url.format(i)
    r = requests.get(target_url)

    sleep(3)

    soup = BeautifulSoup(r.text,'html.parser')

    contents = soup.find_all('div',class_='p0comp-card')
    if len(contents) == 0:
        print(str(len(d_list)+'件しか取得できませんでした。\n'))
        break

    for content in contents:
        title = content.find('div',class_='card__headline--short')
        link = content.find('a',class_='card__link')
        datetime = content.find('time',class_='card__published-date')

        date = datetime.get('datetime').split('T')

        d = {
            'title':title.text,
            'date':date[0],
            'url':link.get('href')
        }

        if keyword == 'NBA':
            d_list.append(d)

        elif keyword in title.text:
            d_list.append(d)
        
        if len(d_list) == n:
            break

    if len(d_list) == n:
        break

    i += 1

df = pandas.DataFrame(d_list)
df.to_excel('{}_news.xlsx'.format(keyword), index=None, encoding='utf-8-sig')
