import time
import numpy as np
from skimage.color import rgb2gray
from skimage import data
import matplotlib.pyplot as plt
from skimage import io
from skimage.viewer import ImageViewer

t = time.clock()
filename = 'gray_image.png' #URL passed in the API call.
image = io.imread(filename)
limit = 240   
bgcolor = image[0,0]   

for a in xrange(0, image.shape[0], 1):
    for b in xrange(0, image.shape[1], 1):
        pixel = image.item(a, b)
        if pixel < limit:
            image.itemset((a, b), bgcolor)
        
viewer = ImageViewer(image)
viewer.show()
tt = time.clock()
print tt-t
