from goose3 import Goose
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords


# nltk.download('stopwords')

# 1 - Importando Artigo da Internet
g = Goose()
url = 'https://blog.geekhunter.com.br/pretensao-salarial-disparidade-generos/'
artigo = g.extract(url)
print(artigo.publish_date)
print(artigo._title)
print(artigo.meta_description)
print(artigo.links)
print(artigo.cleaned_text)

# 2 - Aplicando Ánalise Textual I
word_tokens = word_tokenize(artigo.cleaned_text)
print(word_tokens)
print(len(word_tokens))

portuguese_stops = (set(stopwords.words('portuguese')))

# for palavra in word_tokens:
#     if palavra.lower() not in portuguese_stops:
#         print(palavra)
#         print(len(palavra))

palavras = [palavra for palavra in word_tokens if palavra.lower() not in portuguese_stops]
print(palavras)
print(len(palavras))
