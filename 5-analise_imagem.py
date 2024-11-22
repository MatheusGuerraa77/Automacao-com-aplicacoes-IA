from PIL import Image

# 1 - Imoportando a Imagem / Convertendo a imagem em escala de cinza
img = Image.open('data/homem-aranha.jpg')
# print(img)
# img.show()

gray_img = img.convert('L')
gray_img.show()

# 2 - Utilizando Operações em Imagem
rotated_img = img.rotate(180)
rotated_img.show()

# transpose_img = img.transpote(Image.FLIP_LEFT_RIGHT)
# transpose_img.show()

resize_img_small = img.resize((300,200))
resize_img_small.show()

resize_img_big = img.resize((1500, 1000))
resize_img_big.show()

dim = (200, 200, 250, 300)
crop_img = img.crop(dim)
crop_img.show()