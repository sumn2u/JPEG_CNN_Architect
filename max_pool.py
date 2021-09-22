#Fast implementation of max pooling
def max_pool(image, pool_size=8):
    """
    Fast implementation of max pooling, given the following is true:
    - the length of image shape is 3
    - the image is channels-last
    - pooling height, width, and stride are all equal (pool_size)
    - height % pool_size == 0
    - width % pool_size == 0
    
    Code taken and adjusted from: max_pool_forward_reshape() in https://github.com/mratsim/Arraymancer/issues/174
    """

    height, width, nr_channels = image.shape
    image_reshaped = image.reshape(height // pool_size, pool_size,
                           width // pool_size, pool_size, nr_channels)
    image_mp = image_reshaped.max(axis=1).max(axis=2)
    return image_mp