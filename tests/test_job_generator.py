import unittest

from processor import job_generator
from processor import resize_job


class JobGeneratorTest(unittest.TestCase):

    def test_generates_single_job_for_single_image_and_width(self):
        jobs = job_generator.generate(['/foo/original-a.jpg'], '/bar', [340])
        self.assertEqual([
            resize_job.Job('/foo/original-a.jpg',
                           '/bar/original-a-340w.jpg',
                           new_width=340,
                           new_height=230),
        ], jobs)

    def test_generates_multiple_jobs_for_single_image_and_multiple_widths(self):
        jobs = job_generator.generate(['/foo/original-a.jpg'], '/bar',
                                      [680, 340])
        self.assertEqual([
            resize_job.Job('/foo/original-a.jpg',
                           '/bar/original-a-680w.jpg',
                           new_width=680,
                           new_height=460),
            resize_job.Job('/foo/original-a.jpg',
                           '/bar/original-a-340w.jpg',
                           new_width=340,
                           new_height=230),
        ], jobs)

    def test_generates_multiple_jobs_for_multiple_images_and_single_width(self):
        jobs = job_generator.generate(
            ['/foo/original-a.jpg', '/foo/original-b.jpg'], '/bar', [340])
        self.assertEqual([
            resize_job.Job('/foo/original-a.jpg',
                           '/bar/original-a-340w.jpg',
                           new_width=340,
                           new_height=230),
            resize_job.Job('/foo/original-b.jpg',
                           '/bar/original-b-340w.jpg',
                           new_width=340,
                           new_height=230),
        ], jobs)

    def test_generates_multiple_jobs_for_multiple_images_and_widths(self):
        jobs = job_generator.generate(
            ['/foo/original-a.jpg', '/foo/original-b.jpg'], '/bar', [680, 340])
        self.assertEqual([
            resize_job.Job('/foo/original-a.jpg',
                           '/bar/original-a-680w.jpg',
                           new_width=680,
                           new_height=460),
            resize_job.Job('/foo/original-a.jpg',
                           '/bar/original-a-340w.jpg',
                           new_width=340,
                           new_height=230),
            resize_job.Job('/foo/original-b.jpg',
                           '/bar/original-b-680w.jpg',
                           new_width=680,
                           new_height=460),
            resize_job.Job('/foo/original-b.jpg',
                           '/bar/original-b-340w.jpg',
                           new_width=340,
                           new_height=230),
        ], jobs)
