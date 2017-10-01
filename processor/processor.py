#!/usr/bin/python2

import argparse
import os

from PIL import Image

def dummy():
    pass


def main(args):
    if not os.path.exists(args.output_root):
        os.makedirs(args.output_root)
    for recipe_key in os.listdir(args.input_root):
        image_path = os.path.join(args.input_root, recipe_key, 'main.jpg')
        resized_path = os.path.join(args.output_root, recipe_key + '_thumbnail.jpg')
        image = Image.open(image_path)
        image.thumbnail((340, 230))
        image.convert('RGB').save(resized_path, "JPEG")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='KetoHub Thumbnail Processor',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input_root')
    parser.add_argument('-o', '--output_root')
    main(parser.parse_args())
