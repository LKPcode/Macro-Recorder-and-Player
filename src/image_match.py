import numpy as np
from PIL import Image
import random
import pyautogui as do


class ImageMatch:

    def find_matches(self, haystack, needle):

        haystack = Image.open(haystack)
        needle = Image.open(needle)

        width, height = needle.size
        print(width, height)

        arr_h = np.asarray(haystack)
        arr_n = np.asarray(needle)

        y_h, x_h = arr_h.shape[:2]
        y_n, x_n = arr_n.shape[:2]

        xstop = x_h - x_n + 1
        ystop = y_h - y_n + 1

        matches = []
        for xmin in range(0, xstop):
            for ymin in range(0, ystop):
                xmax = xmin + x_n
                ymax = ymin + y_n

                arr_s = arr_h[ymin:ymax, xmin:xmax]     # Extract subimage
                arr_t = (arr_s == arr_n)                # Create test matrix
                if arr_t.all():                         # Only consider exact matches
                    # get the center of the image
                    matches.append((xmin + width/2, ymin + width/2))

        return matches

    def find_image(self, needle_image):

        #random_name = str(random.randint(0, 1000000000)) + ".png"
        myScreenshot = do.screenshot()
        myScreenshot.save(r'../images/screenshots/desktop.png')

        return self.find_matches("../images/screenshots/desktop.png", "../images/targets/" + needle_image)


# myScreenshot = do.screenshot()
# myScreenshot.save(r'../images/screenshots/desktop.png')
