# Unit test with pytest or python test_utility_functions_9_10.py

from pathlib import Path

from utility_functions_9_5 import *


def test_load_directory_images():
    path = Path(Path.cwd()) / f"data/HST_JWST"
    image_stack, header_stack = load_directory_images(str(path))
    assert image_stack.shape == (5, 2000, 2000)


if __name__ == "__main__":  # used for debugging
    test_load_directory_images()
