import os
import img2pdf
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))


# passed a list of images in img2pdf.convert()
# ends with .jpg
# . means current directory


'''

for i in os.listdir('.'):
    if i.endswith(".jpg"):
        # pass file name or path
        pdf_bytes = img2pdf.convert(i)
        # open 
        file = open(i+".pdf", "wb")
        # write
        file.write(pdf_bytes)
        # close
        file.close()

'''