import os
from skimage.color import rgb2gray
from skimage import data
import matplotlib.pyplot as plt
from skimage import io
from skimage.viewer import ImageViewer
import cv2
import base64

# in NumPy indexing, the first dimension (camera.shape[0]) corresponds to rows, while the second (camera.shape[1])
#  corresponds to columns, with the origin (camera[0, 0]) on the top-left corner. 

# hypothesis: the mean value is the value of the highlight
# Anything between the two extremes counts

filename = 'images/medium.png'
medium_image = io.imread(filename)
gray_image = cv2.cvtColor(medium_image, cv2.COLOR_BGR2GRAY)

# Gets a grayscale image as input

def KeepHighlights(img):
    nRows = img.shape[0] #Number of rows
    nCols = img.shape[1] # opposite to cartesian coordinates
    count = 0
    row = 0
    print ("number of rows: ", nRows)
    print ("number of cols: ", nCols)
    while row < nRows:    
        print(row)
        p = img[row, 0] #beginning of row
        count = 0
        lowerValue = 150 #The (highest) shade of black - most light
        higherValue = 255 #White

        if p > lowerValue and p < higherValue:
            withinRange = True
        else:
            withinRange = False

        # count the number of highlighted pixels in a row

        for i in xrange(0, nCols, 1):
            if (img[row, i] > lowerValue and img[row, i] < higherValue):
                count += 1

        if count == 0:
            for i in xrange(0, nCols, 1):
                img[row, i] = 255
        else:
            start = row

        while count > 0:
            count = 0       
            if (row + 1) < nRows:
                row += 1
                p = img[row, 0]

                for i in xrange(0, nCols, 1):
                    
                    if (img[row, i] > lowerValue and img[row, i] < higherValue):
                        count += 1
            
            if count == 0:
                row -= 1 # every row on top of this is gonna become white
                end = row
                p = img[end, 0]

                for i in xrange(0, nCols, 1):
                    for j in xrange(0, end, 1):
                        p = img[j, i]
                        p = 255
        row += 1

    for row in xrange(1, nRows, 1):
        p = img[row, 0]       
        print ("remove all highlighting - row number ", row)
        for i in xrange(0, nCols, 1):
            if withinRange:
                p = 255

    viewer = ImageViewer(img)
    viewer.show()
    print("Viewer.show() has been implemented, over!")

KeepHighlights(gray_image)


# very handy viewer = ImageViewer(gray_image)
# viewer.show()
