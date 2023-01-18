from PIL import Image

blue = Image.open('blue_color.png')

blue.show

print(blue.filename)

print(blue.size)

pencils = Image.open("pencils.jpg")

pencils.show