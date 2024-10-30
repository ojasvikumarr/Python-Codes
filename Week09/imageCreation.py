import Image 
import nump as np
array1 = np.zeros([100 , 200 , 3] , dtype = np.uint8)
array1[: , :100] = [255 , 128 , 0]
array1[: , 100:] = [0 , 0 , 255]
img = Image.fromarray(array1)
img.save("test1.png")