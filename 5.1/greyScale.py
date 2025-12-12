from PIL import Image

image_beach = Image.open("5.1/kid-green.jpg").load()

def grey(r, g, b):
    grey = int((r+g+b)/3)
    return (grey, grey, grey)

image_output = Image.open("5.1/kid-green.jpg")

for width in range(image_output.width):
    for height in range(image_output.height):
        xy = [width, height]
        image_output.putpixel(xy, grey(image_beach[width, height][0], image_beach[width, height][1], image_beach[width, height][2]))

image_output.save("greyChild.png")