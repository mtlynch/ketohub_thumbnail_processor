#!/usr/bin/python2

import argparse
import logging
import os

from PIL import Image


def dummy():
    pass


logger = logging.getLogger(__name__)


def configure_logging():
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-15s %(levelname)-4s %(message)s',
        '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


def main(args):
    configure_logging()
    if not os.path.exists(args.output_root):
        os.makedirs(args.output_root)
    for root in args.input_root:
        for recipe_key in os.listdir(root):
            image_path = os.path.join(root, recipe_key, 'main.jpg')
            logging.info('Processing %s', recipe_key)
            if not os.path.exists(image_path):
                logging.warning('No image file, skipping')
                continue

            resized_path = os.path.join(args.output_root,
                                        recipe_key + '_thumbnail.jpg')
            image = Image.open(image_path)
            image.thumbnail((340, 230))
            image.convert('RGB').save(resized_path, "JPEG")
            logging.info('Saved resized image to %s', resized_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='KetoHub Thumbnail Processor',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input_root', default=[], action='append')
    parser.add_argument('-o', '--output_root')
    main(parser.parse_args())
