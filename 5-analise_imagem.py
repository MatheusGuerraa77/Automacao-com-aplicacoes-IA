from PIL import Image

# 1 - Imoportando a imagem / convertendo a imagem em escala de cinza
img = Image.open('data/homem-aranha.jpg')
# print(img)
# img.show()

gray_img = img.convert('L')
gray_img.show()