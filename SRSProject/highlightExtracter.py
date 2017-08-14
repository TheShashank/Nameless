import os
from skimage.color import rgb2gray
from skimage import data
import matplotlib.pyplot as plt
from skimage import io
from skimage.viewer import ImageViewer
import cv2
import base64
import ctypes

# in NumPy indexing, the first dimension (camera.shape[0]) corresponds to rows, while the second (camera.shape[1])
#  corresponds to columns, with the origin (camera[0, 0]) on the top-left corner. 

# hypothesis: the mean value is the value of the highlight
# Anything between the two extremes counts

filename = 'images/highlight_ocr.png'
medium_image = io.imread(filename)
gray_image = cv2.cvtColor(medium_image, cv2.COLOR_BGR2GRAY)

# Gets a grayscale image as input
#What if you did it without the p variable?
def KeepHighlights(img):
    '''
    middle of the first row is [503, 1] 
    not [1, 503] ==>
    which is the first column

    '''

    nRows = img.shape[1] #Number of rows, or the Y-coordinate
    nCols = img.shape[0] # Number of columns, or the X-coordinate

    pixelCount = 0
    row = 0
    # average value is going to be the value of the highlight, approximately

    lowerValue = 200 
    higherValue = 210  
    #Changing lowerValue and higherValue seems to have no effect on the colors
    
    def withinRange(number):

        if number > lowerValue:
            if number < higherValue:
                return True
            else:
                return False
        else:
            return False


    while row < nRows:    
        print(row)
        pixelCount = 0 # Number of pixels that fit the criteria for highlighters

        # count the number of highlighted pixels in a row - why?

        for i in xrange(0, nCols, 1):
            p = img[i, row] #image[column, row]

            if withinRange(p):
                pixelCount += 1
                print "count after the initial row loop is: ", pixelCount
        
        # so far, so good

        if pixelCount == 0: # In other words, no pixels were found in this whole row 
                            #- take the average middle row for each line of text
            for i in xrange(0, nCols, 1):
                img[i, row] = 255
                print "A certain pixel has been made white in the second for loop"               
        else:
            start = row
        
        #if highlighted pixels are found, continue until a row where none are found

        while pixelCount > 0:
            pixelCount = 0
            if row + 1 < nRows:
                row += 1
                
                for i in xrange(0, nCols, 1):
                    p = img[i, row]
                    if withinRange(p):
                        pixelCount += 1
            
            #if the pixelCount stayed at 0, i.e. no other highlights in rows
            # Set those areas white
            if pixelCount == 0:
                row -= 1
                end = row

                for i in xrange(0, nCols, 1):
                    p = img[i, row]
                    if withinRange(p) == False:
                        for j in range(start+1, end+1, 1):
                            img[i, j] = 255

            row += 10

        #remove all the highlighting everywhere, leave only text
    for row in xrange(1, nRows, 1):
        for i in xrange(0, nCols, 1):
            p = img[i, row]
            if withinRange(p):
                img[i, row] = 255 # set that particular pixel to white
                # notice how you are smartly not touching the other pixels
                # like in the writing and whatnot    
           
    viewer2 = ImageViewer(img)
    print("Viewer.show() has been implemented, over!")
    viewer2.show()
    
KeepHighlights(gray_image)
# viewer = ImageViewer(gray_image)
# viewer.show()
