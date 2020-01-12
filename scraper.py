import urllib.request
from bs4 import BeautifulSoup
import json
import re
from collections import defaultdict
from pprint import pprint
from unicodedata import normalize
import networkx as nx
from classes import Verse
import os
from pathlib import Path

# url = 'https://www.churchofjesuschrist.org/study/scriptures/bofm/1-ne/1?lang=eng'
# headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}
# request = urllib.request.Request(url,headers=headers)
# html = urllib.request.urlopen(request).read()
def verse_key(book, chapter, verse):
    # return f'{book} {chapter}:{verse}'
    return f'{book} {chapter}'

def main():
    verse_num_re = re.compile(r'note(\d+)([a-z])_')
    # Get a list of all the standard works
    books_list = [line.rstrip() for line in open('books-of-scripture.txt')]
    or_books = '|'.join(books_list)
    reference_re = re.compile(f'({or_books})' + r''
                        r'[.]? '
                        r'(\d+)[:]' # chapter number
                        r'(\d+)'    # verse number
                        r'( ?\(([0-9, -]+)\))?' # extra verses
                        r'', re.IGNORECASE)

    G = nx.DiGraph()

    for root, dirs, files in os.walk(f'wget/www.churchofjesuschrist.org/study/scriptures/'):
        for f in files:
            p = Path(root)
            print('work: {}, book: {}, chapter: {}'.format(
                p.parts[-2], p.parts[-1], f
            ))
            process_chapter(G, os.path.join(root, f), p.parts[-2], p.parts[-1], f)


        # for u, v, fnote in G.edges(data='fnote'):
        #     if fnote == 'b':
        #         print(u, v)
        #         # u.attr = 'found'
        #         print(G.nodes[u]['stdwork'])
        # pprint(G.edges)
        # for node in filter(lambda item: item.book == 'Mosiah', G.nodes):
            # print(node)

        nx.write_gexf(G, './all-refs.gexf', prettyprint=False)


def process_chapter(G, filename, work, book, chapter):
    currentwork = work
    currentbook = book
    currentchapter = chapter
    with open(filename) as html:
        soup = BeautifulSoup(html, 'html.parser')

        # related content is the side panel with all the footnotes
        related_content = soup.select_one('[class|=panelGridLayout]')
        footnotes = related_content.find_all('p')

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
                    # Since multiple consecutive links to the same book do not include
                    # the book name, we prepend the last captured book name and
                    # try to match again
                    if preceding_book:
                        link_text = preceding_book + ' ' + link_text
                        lm = reference_re.match(link_text)
                if not lm:
                    print('Failed to match any for {}'.format(link_text))
                    continue
                orig = verse_key(currentbook, currentchapter, verse_num)
                dest = verse_key(lm.group(1), lm.group(2), lm.group(3))
                G.add_node(orig, book=currentbook, chapter=currentchapter, verse=verse_num, stdwork=currentwork)
                G.add_node(dest, book=lm.group(1), chapter=lm.group(2), verse=lm.group(3))
                G.add_edge(orig, dest, fnote=letter)
                if lm.group(5):
                    G.edges[orig, dest]['additional'] = lm.group(5)
                # G.nodes[orig]['stdwork'] = currentwork



if __name__ == '__main__':
    main()