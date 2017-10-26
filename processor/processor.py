#!/usr/bin/python2

import argparse
import logging
import os

import resize

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
    logger.info('--input_root=%s', args.input_root)
    logger.info('--output_root=%s', args.output_root)
    if not os.path.exists(args.output_root):
        os.makedirs(args.output_root)
    for raw_filename in os.listdir(args.input_root):
        raw_path = os.path.join(args.input_root, raw_filename)
        if os.path.isdir(raw_path):
            continue
        logging.info('Processing %s', raw_path)
        if not os.path.exists(raw_path):
            logging.warning('Could not find image file: %s', raw_path)
            continue

        basename, _ = os.path.splitext(raw_filename)
        resized_path = os.path.join(args.output_root,
                                    basename + '_thumbnail.jpg')
        resize.resize(raw_path, resized_path)
        logging.info('Saved resized image to %s', resized_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='KetoHub Thumbnail Processor',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input_root')
    parser.add_argument('-o', '--output_root')
    main(parser.parse_args())
