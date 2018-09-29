import numpy as np
from skimage import data, color
import matplotlib.pyplot as plt
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte
from scipy.ndimage import imread
import globals
from parseStatus import runRet, parseStatus

def findWormHoles(path):
    locs = []
    image = imread(path,flatten=False,mode='L')
    image = img_as_ubyte(image)
    edges = canny(image, sigma=3, low_threshold=10, high_threshold=50)

    hough_radii = np.arange(5,50,2)
    hough_res = hough_circle(edges, hough_radii)

    accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii, total_num_peaks=45)

    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10,4))
    image = color.gray2rgb(image)
    '''
    radius = 50
    for center_y, center_x in zip(cy, cx):
        circy, circx = circle_perimeter(center_y, center_x, radius)
        image[circy, circx] = (220, 20, 20)
    cx = np.array(cx) * (float(globals.MAPWIDTH)/1028)
    cy = np.array(cy) * (float(globals.MAPHEIGHT)/1028)
    '''
    return np.concatenate((np.atleast_2d(cx),np.atleast_2d(cy)),axis=0)

print(findWormHoles("canvas.png"))