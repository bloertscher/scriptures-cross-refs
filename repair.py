import networkx as nx
import books_of_scripture as bos

G = nx.read_gexf('./all-refs.gexf')
for n, attrs in G.nodes().data():
    try:
        work = attrs['stdwork']
    except KeyError:
        book = attrs['book']
        attrs['stdwork'] = bos.get_stdwork(book)
        work = attrs['stdwork']
        print(f'found work {work} for book {book}')

nx.write_gexf(G, 'repaired-refs.gexf')