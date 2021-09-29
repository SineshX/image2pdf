import os
# import sys
import time

from PIL import Image

# convert all files ending in .jpg inside a directory
dirname = 'data'
imglist = [] #for list of
for fname in os.listdir(dirname):
	if not fname.endswith(".jpg"):
		continue
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue
	imglist.append(Image.open(path).convert('RGB'))

# .convert nahi karoge to encoder error aayega
# imglist.append(path) # yes here


# front image
img1 = Image.open('front.jpg')
img1.convert('RGB')

#convert to pdf
pdfPath='Combined_'+time.strftime("%Y%m%d-%H%M%S")+'.pdf'
# pdfPath='Combine_d.pdf'

img1.save(pdfPath,save_all=True, append_images=imglist)

print('\nconverted\n')
