import os
# import sys
import time

from PIL import Image

# convert all files ending in .jpg inside a directory
dirname = 'D:\Sinesh\Project\img 2 pdf\data'
imglist = [] #for list of
for fname in os.listdir(dirname):
	if not fname.endswith(".png"):
		continue
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue
	imglist.append(Image.open(path).convert('RGB'))

# .convert nahi karoge to encoder error aayega
# imglist.append(path) # yes here

pdfname = input("\nEnter name of the PDF  : ")
# front image
img1 = Image.open('front.png')
img1.convert('RGB')

#convert to pdf
pdfPath= pdfname+time.strftime("%Y%m%d-%H%M%S")+'.pdf'
# pdfPath='Combine_d.pdf'

img1.save(pdfPath,save_all=True, append_images=imglist)

print('\nconverted\n')
