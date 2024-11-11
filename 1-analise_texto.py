import os

# 1 - importação do texto
with open(os.path.join('data', 'texto.txt'), 'r', encoding='utf-8') as file:
    texto = file.read()
    print(texto)
    