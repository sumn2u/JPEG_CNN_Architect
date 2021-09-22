
import numpy as np
#Making 3 channel image by stacking a 1 channel image three times
image_3ch = np.repeat(image_1ch, 3, axis=1).reshape((image_1ch.shape[0], image_1ch.shape[1], 3))