# load in packages
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from linepart import partition_img, convo_edge_det
from img_to_gray import to_gray
from clustering import turnCartoon

# read in image
img = mpimg.imread("../Reef.jpg")

# print out shape of image
imshape = np.shape(img)
print(imshape)
print(img[400:400 + 3, 400:400 + 3, :])
# disp image
plt.imshow(img)
plt.show()

# gray image of clouds
grayimg = to_gray(img, imshape)
plt.imshow(grayimg, cmap='gray', vmin=0, vmax=255)
plt.show()

# edge detected cloud picture
edgemat = convo_edge_det(img, imshape, dlim=30)
plt.imshow(edgemat, cmap="binary", vmin=0, vmax=1)
plt.show()

# cartoonized function
cartimg = turnCartoon(img, edgemat, imshape)
plt.imshow(cartimg)
plt.show()
