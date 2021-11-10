import os
from PIL import Image

FromImgName = 'img'
ToImgName = 'resize'
files = os.listdir(FromImgName)
for file in files:
    img = Image.open(os.path.join(FromImgName, file))
    img_resize = img.resize((600, 800))

    img_resize.save(os.path.join(ToImgName, file))