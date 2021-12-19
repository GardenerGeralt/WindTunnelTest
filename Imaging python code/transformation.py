import numpy as np
from PIL import Image
import csv


with open('Record_2021-12-03_12-29-32.txt', "w") as my_output_file:
    with open('Record_2021-12-03_12-29-32.csv', "r") as my_input_file:
        text_list = []
        for line in my_input_file:
            line = line.split(";")
            text_list.append(", ".join(line))
            my_output_file.writelines(text_list)
    my_output_file.close()

with open('Record_2021-12-03_12-29-32.txt', "r") as f:
    # Read 16-bit RGB565 image into array of uint16
    rgb565array = np.genfromtxt(f, delimiter=',').astype(np.uint16)

# Pick up image dimensions
h, w = rgb565array.shape

# Make a numpy array of matching shape, but allowing for 8-bit/channel for R, G and B
rgb888array = np.zeros([h, w, 3], dtype=np.uint8)

for row in range(h):
    for col in range(w):
        # Pick up rgb565 value and split into rgb888
        rgb565 = rgb565array[row, col]
        r = ((rgb565 >> 11) & 0x1f) << 3
        g = ((rgb565 >> 5) & 0x3f) << 2
        b = ((rgb565) & 0x1f) << 3
        # Populate result array
        rgb888array[row, col] = r, g, b

# Save result as PNG
Image.fromarray(rgb888array).save('result1.png')
