from PIL import Image, ImageDraw
from translate import lookupTableCharacters1, lookupTableCharacters2, lookupTableInstructions

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

def setData(image, scale, data, width, height):
    posX = 3
    posY = 0

    keyType = None
    keyTypeUsed = False

    for key in data:
        color = (0, 0, 0)

        if keyTypeUsed: 
            keyTypeUsed = False
            keyType = None

        if keyType == 0:
            color = lookupTableCharacters1[key][0]
            keyTypeUsed = True
        elif keyType == 1:
            color = lookupTableCharacters2[key][0]
            keyTypeUsed = True

        if keyType == None:
            keyType = key
            color = lookupTableInstructions[key][0]

        setPixel(image, posX, posY, scale, color)
        posX += 1
        if posX == width - 3 and posY < 2:
            posX = 3
            posY += 1
        elif (posX == width - 3 and posY == 2) or (posX == width):
            posX = 0
            posY += 1

def draw(width, height, scale, data):
    image = Image.new('RGB', (width * scale, height * scale), color='white')

    setCorners(image, width, height, scale)
    setData(image, scale, data, width, height)

    return image