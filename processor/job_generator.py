import os

import resize_job


def generate(raw_paths, output_root, widths):
    jobs = []

    for raw_path in raw_paths:
        jobs.extend(_generate_jobs_for_raw_path(raw_path, output_root, widths))

    return jobs


def _generate_jobs_for_raw_path(raw_path, output_root, widths):
    RATIO = 340.0 / 230.0

    jobs = []
    raw_filename = os.path.basename(raw_path)
    basename, _ = os.path.splitext(raw_filename)

    for width in widths:
        height = int(width / RATIO)
        resized_basename = '%s-%dw.jpg' % (basename, width)
        resized_path = os.path.join(output_root, resized_basename)
        jobs.append(resize_job.Job(raw_path, resized_path, width, height))

    return jobs
