from PIL import Image


def create_pixel_dict(image_path, crop_extent=(500, 0, 1720, 1080)):
    """
    Takes image and returns a dictionary with keys as pixel tuples and values containing 
    the number of pixels that matched that tuple

    -------
    keywords

    image_path: path to image location
    crop_extent: a tuple containing a bounding box of (left, upper, right, lower)

    :type image_path : str
    :type crop_extent: tuple

    -----
    returns

    output_dict: dictionary keyed by the pixel tupled. Values contain the number of pixels with that tuple value
    """

    # create output dictionary to hold pixel frequencies keyed by pixel value tuple
    output_dict = {}

    with Image.open(image_path) as traffic_pic:

        # crop using rectangular bounding box defined in crop_extent
        traffic_pic = traffic_pic.crop(box=crop_extent)

        # create list containing the tuple value at each pixel position (flattened)
        pixel_tuple_list = list(traffic_pic.getdata())

        # loop through list, count pixels per unique tuple value and store in output_dict
        for position, pixel_tuple in enumerate(pixel_tuple_list):

            if pixel_tuple in output_dict:
                output_dict[pixel_tuple] += 1

            else:
                output_dict[pixel_tuple] = 1

    return output_dict
