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

image1= Image.open(r'pics\image_manipulator.py\apple.jpeg')
image1.rotate(90).show(r'pics\image_manipulator.py\apple.jpeg')

image2 = Image.open(r'pics\image_manipulator.py\hoop.jpeg')
image2.convert(mode = 'L').show(r'pics\image_manipulator.py\hoop.jpeg')

image10 = Image.open(r'pics\image_manipulator.py\tree.jpeg')
image10.rotate(180).show(r'pics\image_manipulator.py\tree.jpeg')

image11 = Image.open(r'pics\image_manipulator.py\snail.jpeg')
image11.filter(ImageFilter.GaussianBlur(10)).show(r'pics\image_manipulator.py\snail.jpeg')

image12 = Image.open(r'pics\image_manipulator.py\car.jpg')
image12.convert(mode = 'L').show(r'pics\image_manipulator.py\car.jpg')

image13 = Image.open(r'pics\image_manipulator.py\school.jpg')
image13.rotate(20).show(r'pics\image_manipulator.py\school.jpg')

image14 = Image.open(r'pics\image_manipulator.py\phone.jpg')
image14.filter(ImageFilter.GaussianBlur(15)).show(r'pics\image_manipulator.py\phone.jpg')

image15 = Image.open(r'pics\image_manipulator.py\flower.jpg')
image15.convert(mode = 'L').show(r'pics\image_manipulator.py\flower.jpg')

image16 = Image.open(r'pics\image_manipulator.py\chair.jpg')
image16.rotate(90).show(r'pics\image_manipulator.py\chair.jpg')

image17 = Image.open(r'pics\image_manipulator.py\person.jpg')
image17 .show(r'pics\image_manipulator.py\person.jpg')