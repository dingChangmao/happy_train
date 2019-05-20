from time import sleep
from PIL import ImageGrab

# mac使用
m = int(input('请输入想要抓屏几分钟：'))

m = m * 60
n = 1
while n<m:
    sleep(0.02)
    im = ImageGrab.grab()
    local = (r"%s.jpg" % (n))
    im.save(local,'jpeg')
    n = n+1


from PIL import Image
im = Image.open("1.jpg")
images = []
images.append(Image.open('2.jpg'))
images.append(Image.open('3.jpg'))
im.save('gif.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b"aaabb")
