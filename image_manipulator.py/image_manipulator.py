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

image1= Image.open(r'pics\image_manipulator.py\apple.jpg')
image1.rotate(90).show(r'pics\image_manipulator.py\apple.jpg')

image2 = Image.open(r'pics\image_manipulator.py\hoop.jpg')
image2.convert(mode = 'L').show(r'pics\image_manipulator.py\hoop.jpg')

image10 = Image.open(r'pics\image_manipulator.py\tree.jpg')
image10.rotate(180).show(r'pics\image_manipulator.py\tree.jpg')

image11 = Image.open(r'pics\image_manipulator.py\snail.jpg')
image11.filter(ImageFilter.GaussianBlur(10)).show(r'pics\image_manipulator.py\snail.jpg')

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

j_list = ['apple', 'hoop', 'chair', 'snail', 'person', 'car', 'flower', 'phone', 'tree','school']
a_list = ['rotate', 'resize', 'png', 'blur', 'black and white']
def display_list(x):
    for i in x:
        print(i)
    print('')
def run():
    while True:
        print ("Images: ")
        display_list(j_list)
        choice = input("Select image to modify: ")
        if choice.lower() in j_list:
            userImage = Image.open(f"{choice}.jpg")
            userImage.show()
            if userconfirm() == True:
                break
            else:
                print("Invalid Input\n")
        alterimage()

def userconfirm():
    choice = input ('Edit this image? y/n: ').lower()
    if choice == "y":
        return True
    elif choice == 'n':
        print("")
        run()
    else:
        print('invalid input')

def alterimage():
    while True:
        print ("Alter options: ")
        display_list(a_list)
        choice = input('Select alter mode: ')
        choice.lower()
        if choice in a_list:
            if userconfirm() == True:
                if choice == a_list[0]:
                    rotate()
                if choice == a_list[1]:
                    resize()
                if choice == a_list[2]:
                    png()
                if choice == a_list[3]:
                    blur()
                if choice == a_list[4]:
                    blacknwhite()
            