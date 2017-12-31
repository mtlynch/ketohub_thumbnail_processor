import unittest

from processor import resize_job


class JobTest(unittest.TestCase):

    def test_initializes_properties(self):
        job = resize_job.Job(
            '/foo/original_path.jpg',
            '/bar/resized_path-400w.jpg',
            new_width=400,
            new_height=200)
        self.assertEqual('/foo/original_path.jpg', job.raw_path())
        self.assertEqual('/bar/resized_path-400w.jpg', job.resized_path())
        self.assertEqual(400, job.new_width())
        self.assertEqual(200, job.new_height())

    def test_equal_jobs_are_equal(self):
        job_a = resize_job.Job(
            '/foo/original_path.jpg',
            '/bar/resized_path-400w.jpg',
            new_width=400,
            new_height=200)
        job_b = resize_job.Job(
            '/foo/original_path.jpg',
            '/bar/resized_path-400w.jpg',
            new_width=400,
            new_height=200)
        self.assertEqual(job_a, job_b)

    def test_unequal_jobs_are_not_equal(self):
        job_a = resize_job.Job(
            '/foo/original_path.jpg',
            '/bar/resized_path-400w.jpg',
            new_width=400,
            new_height=200)
        job_b = resize_job.Job(
            '/fribby/boo.jpg',
            '/frobby/bing-400w.jpg',
            new_width=800,
            new_height=600)
        self.assertNotEqual(job_a, job_b)
