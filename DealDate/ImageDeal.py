from PIL import Image
import os
import os.path

rootdir = r'D:\picture\success'  # 指明被遍历的文件夹
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)

        im = Image.open(currentPath)
        #进行上下颠倒
        # out = im.transpose(Image.FLIP_TOP_BOTTOM)
        #进行左右颠倒
        # out =out.transpose(Image.FLIP_LEFT_RIGHT)
        # 进行旋转90
        # out = im.transpose(Image.ROTATE_90)
        # 进行旋转180
        # out = im.transpose(Image.ROTATE_180)
        # 进行旋转270
        # out = im.transpose(Image.ROTATE_270)
        #将图片重新设置尺寸
        # out= out.resize((1280,720))
        newname = r"D:\picture\success" + '\\' +"10t"+ filename
        out.save(newname)