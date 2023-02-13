import requests
from bs4 import BeautifulSoup
import time
import csv

perfect_dict = {}

lists = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'y',]

#スクレイピングをする
for i in lists:
    url = f'https://www.jra.go.jp/keiba/overseas/yougo/{i}_list.html'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    terms = soup.findAll('h3') #ok
    meanings = soup.findAll('div', 'txt mt20')

    term_lists = []
    meaning_lists = []

    for i in terms:
        t = i.get_text()
        term_lists.append(t)
        
    del term_lists[-1] 
    del term_lists[-1]
    del term_lists[0]                #整形したterm_lists

    for i in meanings:
        m = i.get_text().strip()
        meaning_lists.append(m)         #整形したmeaning_lists
    
    dict1= dict(zip(term_lists, meaning_lists))
    perfect_dict.update(dict1)

    time.sleep(1)
    
print(perfect_dict)

#TODO:CSVファイルを作成する
with open('dct.csv', 'w') as f:
    writer = csv.writer(f)
    for k, v in perfect_dict.items():
        writer.writerow([k, v])
        