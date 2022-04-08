from PIL import Image, ImageOps

orig = Image.open("./clothing2.jpg")

gray = ImageOps.grayscale(orig)
scale = ImageOps.scale(gray, 0.0373)
inverted = ImageOps.invert(scale)

#inverted.save('new_shirt1.jpg')
inverted.save('new_shirt2.jpg')
#inverted.save('new_bag.jpg')

#scale = ImageOps.scale(gray, 0.02585)
