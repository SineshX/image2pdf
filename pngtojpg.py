from PIL import Image
import os

def png2jpg():
    directory = r'images'
    for f in os.listdir(directory):
        if f.endswith(".png"):
            im = Image.open(os.path.join(directory, f))
            name= os.path.splitext(os.path.join(directory, f))[0] +'.jpg'
            rgb_im = im.convert('RGB')
            rgb_im.save(name)
            print(os.path.join(directory, f))
            continue
        else:
            continue

png2jpg()