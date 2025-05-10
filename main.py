from PIL import Image
from draw import draw
from translate import encode

width, height = 32, 32
scale = 10

data = encode("hello world")
image = draw(width, height, scale)

image.save("output/code.png")
image.show()