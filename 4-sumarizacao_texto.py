from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

# 1 - Coletando o artigo
g = Goose()
url = 'https://olhardigital.com.br/2023/08/07/pro/drex-moeda-digital-e-uma-criptomoeda/'
noticia = g.extract(url)
# print(noticia.cleaned_text)

# 2 - Trabalhando com a Sumarização
parser = PlaintextParser.from_string(
    noticia.cleaned_text,
    Tokenizer('portuguese')
)
# print(parser.document)
sumarizador = LuhnSummarizer()
resumo = sumarizador(
    parser.document,
    2
)
for sentenca in resumo:
    print(sentenca)