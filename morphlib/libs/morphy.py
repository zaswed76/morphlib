import pymorphy2
morph = pymorphy2.MorphAnalyzer()

p = morph.parse('корова')[0]
print(p.tag.POS)


