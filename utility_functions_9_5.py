# Display function doc with help(load_directory_images)

import os
from glob import glob

import numpy as np
from astropy.io import fits


def load_directory_images(path):
    """
    Loads a directory's worth of images into convenient storage units.
    Requires astropy.io.fits, glob.
    Note: All Images in directory must be of same shape.

    Parameters
    ----------
    path: str
        path to the directory you wish to load, as a string.

    Returns
    -------
    image_stack: array_like
        A stack of all images contained in the directory.
        Array of shape (N, X, Y) where N is the number of images,
        and X, Y are the dimensions of each image.
    image_dict: dict
        A dictionary containing headers for each image, the keys
        are the same as the indices of the corresponding
        image in the image_stack
    """
    if not isinstance(path, str):
        raise AssertionError("Path must be a string.")
    if os.path.isdir(path) == False:
        raise OSError("Path does not point to a valid location.")

    files_in_dir = glob(path + "/*")
    image_stack = []
    header_stack = {}
    for i, f in enumerate(files_in_dir):
        with fits.open(f) as HDU:
            image_stack.append(HDU[0].data)
            header_stack[i] = HDU[0].header
    image_stack = np.array(image_stack)
    return image_stack, header_stack
