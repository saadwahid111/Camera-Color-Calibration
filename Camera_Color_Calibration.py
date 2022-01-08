def gamma_correction(img, correction):
    img = img/255.0
    img = cv2.pow(img, correction)
    return np.uint8(img*255)
 
# 24 color patches of Xrite color checker passport are utilized as testing color samples. 
# The color patches are extracted by using Canny Edge Detection and are our samples are more 
# refined by extracting our region of interest (ROI) at the center of each color patch.


import cv2
import numpy as np
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from skimage import feature
image=cv2.imread('opencv_frame_5.png')
plt.imshow(image)
plt.show()
original = image.copy()
image = gamma_correction(image, 0.5)
#image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5 , 5), 0)
gray = cv2.bitwise_not(gray)
edged = cv2.Canny(gray, 60, 10)
plt.imshow(edged)
plt.show()
#cv2.imwrite('f.png', edged)
_, contours, _=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)




def exct(ROI):
    [rows, cols, n] = ROI.shape
    #ROI = ROI[30:60,30:60]
    M = np.zeros([20,20,3])
    x=0
    for i in range(rows):
        for j in range(cols):
            k = ROI[i,j]
            if np.any(k) != 0:
                M[x]=k
        x=x+1
        if x==20:
            break
    M = M.astype(int)

    return M
