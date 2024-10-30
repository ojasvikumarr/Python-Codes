from PIL import Image 

im = Image.open("test.png")
rgb_im = im.convert('RGB')

rbgValue = rgb_im.getpixel(150, 0)
