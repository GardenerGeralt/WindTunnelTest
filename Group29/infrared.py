import glob
import os
from multiprocessing import Pool

import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import uniform_filter1d
from PIL import Image

# Distance in px from LE/TE in which transition will not be detected
# Necessary to prevent LE/TE to be detected as transition point
EDGE_CUTOFF = 5


def load_infrared_from_file(folder):
    individual_data = []
    for file in glob.glob(f"{folder}/*.csv"):
        # Remove last column which is NaN
        individual_data.append(np.delete(np.genfromtxt(file, delimiter=";"), -1, axis=1))

    # Average all images in the folder
    averaged_data = np.average(individual_data, axis=0)

    # Normalize to [0, 1] as required by Pillow
    min_temp = averaged_data.min()
    max_temp = averaged_data.max()
    range_temp = max_temp - min_temp
    averaged_data = (averaged_data - min_temp) / range_temp

    image = Image.fromarray(np.uint8(averaged_data * 255))
    # Rotate so LE and TE are vertical
    image = image.rotate(-1.2, resample=Image.BICUBIC)
    # Crop for clear image of wing without wall and lower tuft
    image = image.crop((50, 30, image.width - 80, image.height - 130))
    # Flip so flow comes from left
    image = image.transpose(method=Image.FLIP_LEFT_RIGHT)

    # Scale up to real temperature range
    processed_image = np.array(image)
    processed_image = processed_image / 255 * range_temp + min_temp

    return processed_image, image.height


def find_transition_point(image):
    # Average along span to get single chordwise line
    spanwise_average = np.average(image, axis=0)
    # Find pixel-by-pixel difference along chord
    chordwise_difference = np.diff(spanwise_average)
    # Moving average with window size 3
    chordwise_difference = uniform_filter1d(chordwise_difference, size=3)

    # Crop image to wing without background
    x_leading_edge = chordwise_difference.argmax()
    x_trailing_edge = chordwise_difference.argmin()
    chordwise_difference = chordwise_difference[
                           x_leading_edge + EDGE_CUTOFF: x_trailing_edge - 2 * EDGE_CUTOFF
                           ]

    chord_length = x_trailing_edge - x_leading_edge

    # Find x/c of transition
    xc_transition = (chordwise_difference.argmin() + EDGE_CUTOFF) / chord_length

    # Convert to image coordinates for line in plot
    x_transition = x_leading_edge + xc_transition * chord_length

    return xc_transition, x_transition, x_leading_edge, x_trailing_edge


def plot_infrared_image(folder, prefix, alpha):
    image, height = load_infrared_from_file(folder)

    xc_transition, x_transition, x_leading_edge, x_trailing_edge = find_transition_point(image)

    plt.imshow(image, cmap="inferno", interpolation="none")

    plt.text(x_leading_edge - 5, height - 10, "LE", ha="right")
    plt.text(x_trailing_edge + 5, height - 305, f"Alpha = {alpha} [deg]")
    plt.text(x_trailing_edge + 5, height - 10, "TE")
    # plt.text()
    # No clear transition beyond 15.5 deg and for hysteresis part
    # Only for 2D because 3D has curved transition line
    '''if (
            (prefix == "2D")
            and ("back" not in alpha)
            and (alpha[0] == "-" or float(alpha.split("-")[0]) <= 15.5)
    ):
        plt.axvline(x_transition, c="black", linestyle=(0, (1, 10)))
        plt.text(x_transition + 10, 20, f"x/c = {xc_transition:.2f}")'''

    plt.axis("off")
    plt.gcf().tight_layout(pad=0.1, h_pad=0.4, w_pad=0.4)

    plt.show()


def plot_infrared_image_all_alphas(folder, prefix):
    p = Pool()

    folder = f"{folder}"
    for alpha in os.listdir(folder):
        full_path = os.path.join(folder, alpha)
        if os.path.isdir(full_path) and os.listdir(full_path):
            p.apply_async(plot_infrared_image, args=(full_path, prefix, alpha))

    p.close()
    p.join()


if __name__ == "__main__":
    # plot_infrared_image_all_alphas("2dIR", "2D")
    # plot_infrared_image_all_alphas("IR2d", "2D")
    plot_infrared_image("IR2D/0", "2D", "0")
