from PIL import Image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

def is_green(r, g, b):
    if 0<=r<40 and 215<g<=255 and 0<=b<40:
        return True
    else:
        return False

# def colour(r, g, b):
#     if 230<=r<255 and 0<=g<25 and 0<=b<25:
#         return "Red"
#     elif 0<=r<25 and 230<=g<255 and 0<=b<25:
#         return "Green"
#     elif 0<=r<25 and 0<=g<25 and 230<=b<255:
#         return "Blue"
#     elif 230<=b<255 and 230<=b<255 and 230<=b<255:
#         return "White"
#     elif 0<=r<25 and 0<=g<25 and 0<=g<25:
#         return "Black"
#     elif 230<=b<255 and 230<=b<255 and 0<=g<25:
#         return "Yellow"
#     elif 230<=b<255 and 0<=g<25 and 230<=b<255:
#         return "Magenta"
    
image_output = Image.open("5.1/kid-green.jpg")

for width in range(image_output.width):
    for height in range(image_output.height):
        if is_green(image_green[width, height][0], image_green[width, height][1], image_green[width, height][2]):
            xy = [width, height]
            image_output.putpixel(xy, image_beach[width, height])

image_output.save("output.png")