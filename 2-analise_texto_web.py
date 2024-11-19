from goose3 import Goose

# 1 - Importando Artigo da Internet
g = Goose()
url = 'https://blog.geekhunter.com.br/pretensao-salarial-disparidade-generos/'
artigo = g.extract(url)
print(artigo.publish_date)
print(artigo._title)
print(artigo.meta_description)
print(artigo.links)
print(artigo.cleaned_text)