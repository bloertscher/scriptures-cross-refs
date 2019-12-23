from books_of_scripture import books_of_scripture

class Verse:
    """ A single verse entity
    """

    def __init__(self, book, chapter, verse_no):
        self.book = book
        self.chapter = chapter
        self.verse_no = verse_no

    # https://stackoverflow.com/a/2909119
    def __key(self):
        return (self.book, self.chapter, self.verse_no)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Verse):
            return self.__key() == other.__key()
        return NotImplemented

    def __repr__(self):
        return '{}'.format(self.__key())

    def __lt__(self, other):
        return books_of_scripture.index(self.book.lower()) < books_of_scripture.index(other.book.lower()) or self.chapter < other.chapter or self.verse_no < other.verse_no



class Reference:
    """ A single reference from one Verse to another
    """

    def __init__(self, orig, dest):
        self.orig = orig
        self.dest = dest

    def __eq__(self, other):
        if isinstance(other, Reference):
            return self.orig == other.orig and self.dest == other.dest
        return NotImplemented

    def __key(self):
        return (self.orig, self.dest)

    def __hash__(self):
        return hash(self.__key())

    def __repr__(self):
        return '{} -> {}'.format(self.orig, self.dest)

    def __lt__(self, other):
        return self.orig < other.orig or self.dest < other.dest


def main():
    from pprint import pprint
    v = Verse('1 Ne', '1', '7')
    w = Verse('2 Ne', '3', '8')

    r = Reference(v, w)
    q = Reference(w, v)

    s = set()
    s.add(v)
    s.add(w)
    s.add(w)
    pprint(s)

    rs = set()
    rs.add(r)
    rs.add(q)
    pprint(rs)
    print(Reference(Verse('1 Ne', '1', '7'), Verse('2 Ne', '3', '8')) in rs)

    l = list([v, w, Verse('1 Ne', '1', '6')])
    l = sorted(l)
    pprint(l)

    h = list([q, r])
    h = sorted(h)
    pprint(h)

if __name__ == '__main__':
    main()