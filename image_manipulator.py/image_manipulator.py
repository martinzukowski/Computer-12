#image manipulator
from PIL import Image, ImageFilter
import os

size_300 = (300,300)
size_700 = (700,700)


for f in os.listdir('.'):
    if f.endswith('.jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splittext(f)

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn,fext))

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn,fext))

image1= Image.open('apple.jpeg')
image1.rotate(90).show('apple.jpeg')

image2 = Image.open('hoop.jpeg')
image2.convert(mode = 'L').show("hoop.jpeg")

image10 = Image.open('tree.jpeg')
image10.rotate(180).show('tree.jpeg')

image11 = Image.open('snail.jpeg')
image11.filter(ImageFilter.GaussianBlur(10)).show('snail.jpeg')

image12 = Image.open('car.jpg')
image12.convert(mode = 'L').show('car.jpg')

image13 = Image.open('school.jpg')
image13.rotate(20).show('school.jpg')

image14 = Image.open('phone.jpg')
image14.filter(ImageFilter.GaussianBlur(15)).show('phone.jpg')

image15 = Image.open('flower.jpg')
image15.convert(mode = 'L').show('flower.jpg')

image16 = Image.open('chair.jpg')
image16.rotate(90).show('chair.jpg')

image17 = Image.open('person.jpg')
image17 .show('person.jpg')