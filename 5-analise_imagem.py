from PIL import Image

# 1 - Imoportando a Imagem / Convertendo a imagem em escala de cinza
img = Image.open('data/homem-aranha.jpg')
# print(img)
# img.show()

gray_img = img.convert('L')
gray_img.show()