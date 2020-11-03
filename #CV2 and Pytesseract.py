#CV2 and Pytesseract

import cv2
import pytesseract
from PIL import Image, ImageOps
lst=[101,151,201,251,301,351]


'''
def white_bg_square(img):
    #"returns a white-background-color image having the img in exact center"
    size = (max(img.size),)*2
    layer = Image.new('RGB', size, (255,255,255))
    layer.paste(img, tuple(map(lambda x:(x[0]-x[1])/2, zip(size, img.size))))
    return layer
'''
def lir1():
	for i in range(6):
		scn="scene"
		end=".png"
		zero="00"
		my_str=scn+zero+str(lst[i])+end
		print(my_str)

		im = Image.open(my_str)

		width, height = im.size 
		#print(im.size)
		# Setting the points for cropped image 
		left = 305
		top = 880
		right = 700
		bottom = 950
		  
		# Cropped image of above dimension 
		# (It will not change orginal image) 
		im1 = im.crop((left, top, right, bottom))
		im1_inv=ImageOps.invert(im1)
		im1_gray=im1_inv.convert('L')
		
		  
		# Shows the image in image viewer 
		im1_gray.show()
		im1_gray.save('prcd.png')

		#im1_gray_rs1=Image.open('prcd.png')
		#im1_gray_rs=white_bg_square(im1_gray_rs1)

		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

		#img=cv2.imread('scene00051.png')
		img=cv2.imread('prcd.png')
		prcd=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		(thresh, bwi)=cv2.threshold(prcd, 127, 255, cv2.THRESH_BINARY)
		cv2.imshow('Black white image', bwi)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


		#rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

		text = pytesseract.image_to_string(img)
		print("text read:",text.split())
		proc_txt=text.split()


lir1()


