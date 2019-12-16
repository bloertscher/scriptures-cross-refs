import urllib.request
from bs4 import BeautifulSoup
import json
import re
from collections import defaultdict
from pprint import pprint
from unicodedata import normalize

# url = 'https://www.churchofjesuschrist.org/study/scriptures/bofm/1-ne/1?lang=eng'
# headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}
# request = urllib.request.Request(url,headers=headers)
# html = urllib.request.urlopen(request).read()

verse_num_re = re.compile(r'note(\d+)([a-z])_')
# Get a list of all the standard works
books_list = [line.rstrip() for line in open('books-of-scripture.txt')] 
or_books = '|'.join(books_list)
reference_re = re.compile(f'({or_books})'
                      '[.]* '
                      '(\\d+)[:]'
                      '(\\d+.*)'
                      '', re.IGNORECASE)

with open('wget/www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/3') as html:
    soup = BeautifulSoup(html, 'html.parser')

    related_content = soup.select_one('[class|=panelGridLayout]')
    footnotes = related_content.find_all('p')
    footnotes_by_verse_num = defaultdict(lambda: defaultdict(list))
    for footnote in footnotes[:]:
        # extract the verse number from the <p id=note1d_p1> 
        m = verse_num_re.match(footnote['id'])
        if not m:
            print('Failed to match verse number for "{}"'.format(footnote['id']))
            continue
        verse_num = m.group(1) 
        letter = m.group(2)
        links = footnote.find_all('a')
        preceding_book = None
        for link in links:
            link_text = normalize('NFKD', link.get_text())
            lm = reference_re.match(link_text)
            if lm:
                preceding_book = lm.group(1)
            if not lm:
                if preceding_book:
                    link_text = preceding_book + ' ' + link_text
                    lm = reference_re.match(link_text)
            if not lm:
                print('Failed to match any for {}'.format(link_text))
                continue
            print('Book: {}, Chapter: {}, Rest: {}'.format(lm.group(1), lm.group(2), lm.group(3)))
            footnotes_by_verse_num[verse_num][letter].append(link_text)

        # print('verse number ' + verse)
        # print(footnote.prettify())
    # pprint(footnotes_by_verse_num)

    # links = footnotes[2].find_all('a')
    # print(links)

    # { std_work : BoM, 
    #    
    # }