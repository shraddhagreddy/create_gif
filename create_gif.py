""" so v3 is the version 3 of image io and iio is the shorter name we have given it in order to access it easily.

"""
import imageio.v3 as iio

filenames=["team-pic1.png", "team-pic2.png"]
filenames1=["chicklet1.png","chicklet2.png","chicklet3.png","chicklet4.png"]
images=[]
images2=[]

for filename in filenames:
    images.append(iio.imread(filename))
    #The .imread() method loads an image based on the file path. So now, our images variable has all the images!
iio.imwrite("team.gif", images, duration= 500, loop=0)

for filename in filenames1:
    images2.append(iio.imread(filename))
iio.imwrite("chicklet.gif", images2, duration=500, loop=0)