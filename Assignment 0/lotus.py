from imageio import *
import matplotlib.pyplot as plt

im = imread('lotus.jpg')
plt.axis('off')
plt.imshow(im)
plt.show()
