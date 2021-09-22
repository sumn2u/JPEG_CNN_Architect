import numpy as np
#Convert an RGB image to a greyscale image
def rgb_to_greyscale(image):
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])