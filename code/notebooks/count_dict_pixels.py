def count_dict_pixels(label_dict, image_array, alpha=255):
    """takes in a dictionary of tuples with values as pixel values,
    labels as keys, and counts the images in a pixel that fall under each key"""
    if image_array.dtype == 'float32':

        # create dictionary for pixel counts by key
        output_dict = {}

        # convert values from 0-1 space to 0-255 space
        image_array = image_array * 255

        for key, value in label_dict.items():
            r, g, b = value

            # red channel
            ar_temp_r = np.zeros(image_array[:, :, 0].shape)
            r_true = np.where(image_array[:, :, 0] == r)
            ar_temp_r[r_true] = 1

            # green channel
            ar_temp_g = np.zeros(image_array[:, :, 1].shape)
            g_true = np.where(image_array[:, :, 1] == g)
            ar_temp_g[g_true] = 1

            # blue channel
            ar_temp_b = np.zeros(image_array[:, :, 2].shape)
            b_true = np.where(image_array[:, :, 2] == b)
            ar_temp_b[b_true] = 1

            # alpha channel
            ar_temp_alpha = np.zeros(image_array[:, :, 2].shape)
            alpha_true = np.where(image_array[:, :, 3] == alpha)
            ar_temp_alpha[alpha_true] = 1

            # multiplying results in binary matrix where rgba = the specified value tuple
            mask_array = ar_temp_r * ar_temp_g * ar_temp_b * ar_temp_alpha

            # sum results in number of pixels matching rgba value
            pixel_count = mask_array.sum()

            # update output dict with pixel count
            output_dict[key] = pixel_count

    else:
        print(
            'image array dtype is not float32 or float64 (values ranging from 0-1). change to float32 array before use'
        )
    return output_dict