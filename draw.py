from PIL import Image, ImageDraw

def rect(image, x, y, sx, sy, c):
    for i in range(sx):
        for j in range(sy):
            image.putpixel((x + i, y + j), c)

def setPixel(image, x, y, scale, c):
    rect(image, x * scale, y * scale, scale, scale, c)

def setCorners(image, width, height, scale):
    setPixel(image, 0, 0, scale, (255, 0, 0))
    setPixel(image, 1, 0, scale, (0, 0, 255))
    setPixel(image, 0, 1, scale, (0, 255, 0))

    setPixel(image, 1, height - 1, scale, (0, 255, 0))
    setPixel(image, 0, height - 2, scale, (0, 0, 255))
    setPixel(image, 1, height - 2, scale, (255, 0, 0))

    setPixel(image, width - 1, 0, scale, (255, 0, 0))
    setPixel(image, width - 2, 0, scale, (0, 0, 255))
    setPixel(image, width - 1, 1, scale, (0, 255, 0))

    setPixel(image, width - 1, height - 1, scale, (255, 0, 0))
    setPixel(image, width - 2, height - 1, scale, (0, 0, 255))
    setPixel(image, width - 1, height - 2, scale, (0, 255, 0))

def draw(width, height, scale):
    image = Image.new('RGB', (width * scale, height * scale), color='white')

    setCorners(image, width, height, scale)

    return image