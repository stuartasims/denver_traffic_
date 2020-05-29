from matplotlib import image


def trim_image_xy(image_path, top=0, bottom=0, left=0, right=0):
    """trim an image at specified path by rows on left and right edge and by columns on top and bottom"""

    #read in image
    im1 = image.imread(image_path)

    #capture shape of numpy array
    rows, cols, depth = im1.shape

    #clip and store
    image_clip = im1[top:(rows-bottom), left:(cols-right), :]

    return image_clip