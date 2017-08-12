import cv2
import numpy as np 
from matplotlib import pyplot as plt

#end with cv2.imwrite or something of that nature


def KeepHighlightsOnly(img, r, g, b): #convert r, g, b to intensities? 0 is black
  channels = img.shape[2]
  nCols = img.shape[1]*channels #Y
  nRows = img.shape[0] #X
  
  count = 0
  row = 0

  while (row < nRows):
    p = img.item(row, 0, 0)
    count = 0

    for i in xrange(0, nCols-3, 3):
      if (img[row, i, 0] == b and img[row, i, 1] == g and img[row, i, 2] == r):
        count += 1
    
    # we are going row by row

    if count == 0:
      for i in xrange(0, nCols, 1):
        img.itemset((row, i, 0), 255) #doesn't make sense

    else: 
      start = row
    
    while count > 0:
      count = 0
      #same thing all over again
      #we want to find another row without highlights tho

      if row + 1 < nRows:
        row += 1
        p = img[row, :, :]

        for i in xrange(0, nCols-3, 3):
          if (img[row, i, 0] == b and img[row, i, 1] == g and img[row, i, 2] == r):
            count += 1

      if count == 0:
        row -= 1
        end = row
        p = img.item(end, 0, 0)

        for i in xrange(0, nCols-3, 3):
          if (img[row, i, 0] != b and img[row, i, 1] != g and img[row, i, 2] != r):
            for j in xrange(start+1, end+1, 1):
              p = img.item(row, j, 0)
              img.itemset((row, j, 0), 255)
              img.itemset((row, j, 1), 255)
              img.itemset((row, j, 2), 255)
    row += 1 


  #remove all the highlighting, leaving only the text that was initially highlighted
  for row in xrange(1, nRows, 1):
    p = img.item(row, 0, 0)

    for i in xrange(0, nCols-3, 3):
      if img[row, i, 0] == b and img[row, i, 1] == g and img[row, i, 2] == r:
        img.itemset((row, j, 0), 255)
        img.itemset((row, j, 1), 255)
        img.itemset((row, j, 2), 255)

  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


  plt.subplot(231),plt.imshow(img,'gray'),plt.title('not-ORIGINAL')
  print("What just happened?")
  plt.show()

myimage = cv2.imread('images/highlight_ocr.png')

KeepHighlightsOnly(myimage, 251, 226, 152)
