import urllib.request
from bs4 import BeautifulSoup
import json
import re
from collections import defaultdict

url = 'https://www.churchofjesuschrist.org/study/scriptures/bofm/1-ne/1?lang=eng'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}
request = urllib.request.Request(url,headers=headers)
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html, 'html.parser')

related_content = soup.select_one('[class|=panelGridLayout]')
footnotes = related_content.find_all('p')
footnotes_by_verse_num = defaultdict(list)
verse_num_re = re.compile(r'note(\d+)')
for footnote in footnotes[:3]:
    verse = verse_num_re.match(footnote['id']).group(1)
    footnotes_by_verse_num[int(verse)].append(footnote.find_all('a'))
    # print('verse number ' + verse)
    links = footnote.find_all('a')
    # print(footnote.prettify())
print(footnotes_by_verse_num)

# links = footnotes[2].find_all('a')
# print(links)

# { std_work : BoM, 
#    
# }