#!/usr/bin/python2

import argparse
import logging
import os

import resize
import job_generator
import supported_file

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

    raw_paths = _get_raw_image_paths(args.input_root)
    jobs = job_generator.generate(raw_paths,
                                  args.output_root,
                                  widths=(680, 560, 340))
    _process_jobs(jobs)


def _get_raw_image_paths(input_root):
    return filter(supported_file.is_supported,
                  [os.path.join(input_root, f) for f in os.listdir(input_root)])


def _process_jobs(jobs):
    for job in jobs:
        if not os.path.exists(job.raw_path()):
            logging.warning('Could not find image file: %s', job.raw_path())
            continue
        if os.path.exists(job.resized_path()):
            continue
        logging.info('Processing %s', job.raw_path())
        resize.resize(job)
        logging.info('Saved resized image to %s', job.resized_path())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='KetoHub Thumbnail Processor',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input_root', required=True)
    parser.add_argument('-o', '--output_root', required=True)
    main(parser.parse_args())
