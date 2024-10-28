from PIL import Image 

img = Image.open("Week08/lena.jpg")

transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# save it to a human understandable Image
transposed_img.save("resolved_img.jpg")