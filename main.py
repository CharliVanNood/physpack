from PIL import Image
from draw import draw
from translate import encode

width, height = 32, 32
scale = 10

data = encode("print(\"\")")
image = draw(width, height, scale, data)

image.save("output/code.png")
image.show()