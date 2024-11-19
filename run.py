import argparse
import os
import random
import sys
from datetime import datetime

from PIL import Image


def generate_random_color_image(width, height, output_dir, color=None):
    date = datetime.now().strftime("%Y%m%d")

    if color is None:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color_hex = f"{color[0]:02x}{color[1]:02x}{color[2]:02x}".upper()
    else:
        color_hex = color.upper()
        color = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))

    filename = f"{date}_{color_hex}_{width}x{height}.png"

    image = Image.new("RGB", (width, height), color)

    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    image.save(filepath)
    print(f"Image saved as {filepath} with size {width}x{height} and color {color}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate images with random or specified colors and dimensions.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-c", "--color", help="Specify the color in 6-character hex (e.g., ffffff).", type=str)
    parser.add_argument("-s", "--size", help="Specify the size of the image as width and height (e.g., -s 800 600).", nargs=2, type=int, required=True)
    parser.add_argument("-n", "--number", help="Number of random images to generate (ignored if color is specified).", type=int, default=1)
    parser.add_argument("-d", "--dir", help="Specify the output directory (default: current directory).", type=str, default=".")

    args = parser.parse_args()

    width, height = args.size

    if args.color:
        if len(args.color) != 6 or not all(c in "0123456789abcdefABCDEF" for c in args.color):
            print("Error: Invalid color format. Please provide a valid 6-character hex color (e.g., ffffff).")
            sys.exit(1)
        generate_random_color_image(width, height, args.dir, args.color)
    else:
        if args.number < 1:
            print("Error: Number must be a positive integer.")
            sys.exit(1)
        for _ in range(args.number):
            generate_random_color_image(width, height, args.dir)


if __name__ == "__main__":
    main()
