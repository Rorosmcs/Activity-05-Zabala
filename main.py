import cv2 as cv
import numpy as py


img = cv.inread("robs.jpg")


if(len(img.shape)<2):
    print("\nImage Type: Grayscale Image")
    exit()
elif len(img.shape)==3:
    print("\nImage Type: Colored Image")


maxheight =  1920
maxwidth = 1080
minheight = 480
minwidth = 360
size = 1500000


print("\nImage Dimension limit : max = 1920 x 1080 and min = 480 x 360")
imgheight = img.shape[0]
imgwidth = img.shapre[1]
print("Current loaded image dimension:", imgheight, "x",imgwidth)
if((imgheight < maxheight and imgheight > minheight) and (imgwidth < maxwidth and imgwidth > minwidth)):
    print("Current loaded image is within the boundaries!")
else:
    print("Current loaded image is not in the boundaries!")


print("\nSet size:", size)
imgsize = img.size
print("Current loaded image size:",imgsize)
if(imgsize < size):
    print("Current loaded image has lower pixel count than the set image size!")
else:
    print("\nCurrent loaded image has higher pixel count than the set image size!")

print("\nCurrent loaded image datatype:", img.dtype)


print("\nAccess a pixel value using item method")
b,n,m = input("Enter row, column and channel: ").split() 
row1,colm1,chann1 = [int(b), int(n), int (m)]
res = img.item(row1,colm1,chann1)
print("Result: ".res)

print("\n Modify a pixel value using Itemset method")
o,p = input("Enter column and row: ").split()
blue = int(input("Enter changes in blue channel: "))
green = int(input("Enter changes in green channel: "))
red = int(input("Enter changes in red channel: "))
print("Result: ")
row2, colm2 = [int(o), int(p)]
img.item(row2,colm2,0)
img.item(row2,colm2,1)
img.item(row2,colm2,2)
res1 = img[row2,colm2]
print("Before:", res1)
img.itemset((row2,colm2,0), blue)
img.itemset((row2,colm2,0), green)
img.itemset((row2,colm2,0), red)
res2 = img[row2,colm2]
print("After: ", res2,"\n")