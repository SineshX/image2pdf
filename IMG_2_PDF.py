import os
import img2pdf
import time

''' To Convert multiple image of a folder (images here) into a single pdf  (Combined.pdf) '''

pdf_path = 'Combined_'+time.strftime("%Y%m%d-%H%M%S")+'.pdf'
with open(pdf_path, 'wb') as f:
    #  for all .jpg  in data folder
    try:
        f.write(img2pdf.convert(["images/"+i for i in os.listdir('images') if i.endswith(".jpg") ]) )
        print('Converted :)\n')
        
    except ValueError:
        print("Please put all images in images folder")

# TODO img2pdf.AlphaChannelError: with .png files for now
# RGBA



''' To Convert each image of a folder(data here) into a single-single pdf (fileNameOfjpg.pdf)'''


# for i in os.listdir('images'):
#     if i.endswith(".jpg"):
#         # pass file name or path
#         pdf_bytes = img2pdf.convert("images/"+i)
#         # open 
#         file = open("pdf/"+i+".pdf", "wb")
#         # write
#         file.write(pdf_bytes)
#         # close
#         file.close()


# if u wanna use use a fancy name and also avoid overwriting : use
# pdf_path= i+time.strftime("%Y%m%d-%H%M%S")+'.pdf'
# file = open(pdf_path, "wb")