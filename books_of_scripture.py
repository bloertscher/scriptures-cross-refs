
def get_stdwork(abbrev_book):
    if abbrev_book == 'D&C':
        return 'dc-testament'
    idx = books_abbrev.index(abbrev_book)
    if idx >= books_abbrev.index('Gen') and idx <= books_abbrev.index('Mal'):
        return 'ot'
    if idx >= books_abbrev.index('Matt') and idx <= books_abbrev.index('Rev'):
        return 'nt'
    if idx >= books_abbrev.index('1 Ne') and idx <= books_abbrev.index('Moro'):
        return 'bofm'
    if idx >= books_abbrev.index('Moses') and idx <= books_abbrev.index('A of F'):
        return 'pgp'
    raise ValueError



"""The names of books in the filepath"""
lower_books_abbrev = [
'gen',
'ex',
'lev',
'num',
'deut',
'josh',
'judg',
'ruth',
'1-sam',
'2-sam',
'1-kgs',
'2-kgs',
'1-chr',
'2-chr',
'ezra',
'neh',
'esth',
'job',
'ps',
'prov',
'eccl',
'song',
'isa',
'jer',
'lam',
'ezek',
'dan',
'hosea',
'joel',
'amos',
'obad',
'jonah',
'micah',
'nahum',
'hab',
'zeph',
'hag',
'zech',
'mal',
'matt',
'mark',
'luke',
'john',
'acts',
'rom',
'1-cor',
'2-cor',
'gal',
'eph',
'philip',
'col',
'1-thes',
'2-thes',
'1-tim',
'2-tim',
'titus',
'philem',
'heb',
'james',
'1-pet',
'2-pet',
'1-jn',
'2-jn',
'3-jn',
'jude',
'rev',
'1-ne',
'2-ne',
'jacob',
'enos',
'jarom',
'omni',
'w-of-m',
'mosiah',
'alma',
'hel',
'3-ne',
'4-ne',
'morm',
'ether',
'moro',
'dc',
'moses',
'abr',
'js-m',
'js-h',
'a-of-f'
]

""" The names of books as in references """
books_abbrev = [
'Gen',
'Ex',
'Lev',
'Num',
'Deut',
'Josh',
'Judg',
'Ruth',
'1 Sam',
'2 Sam',
'1 Kgs',
'2 Kgs',
'1 Chr',
'2 Chr',
'Ezra',
'Neh',
'Esth',
'Job',
'Ps',
'Prov',
'Eccl',
'Song',
'Isa',
'Jer',
'Lam',
'Ezek',
'Dan',
'Hosea',
'Joel',
'Amos',
'Obad',
'Jonah',
'Micah',
'Nahum',
'Hab',
'Zeph',
'Hag',
'Zech',
'Mal',
'Matt',
'Mark',
'Luke',
'John',
'Acts',
'Rom',
'1 Cor',
'2 Cor',
'Gal',
'Eph',
'Philip',
'Col',
'1 Thes',
'2 Thes',
'1 Tim',
'2 Tim',
'Titus',
'Philem',
'Heb',
'James',
'1 Pet',
'2 Pet',
'1 Jn',
'2 Jn',
'3 Jn',
'Jude',
'Rev',
'1 Ne',
'2 Ne',
'Jacob',
'Enos',
'Jarom',
'Omni',
'W of M',
'Mosiah',
'Alma',
'Hel',
'3 Ne',
'4 Ne',
'Morm',
'Ether',
'Moro',
'D&C',
'Moses',
'Abr',
'JS—M',
'JS—H',
'A of F'
]

# lower_works_abbrev = [
# 'bofm',
# 'dc-testament',
# 'nt',
# 'ot',
# 'pgp'
# ]

# works_abbrev = [
# 'BofM',
# 'D&C',
# 'NT',
# 'OT',
# 'PGP'
# ]
