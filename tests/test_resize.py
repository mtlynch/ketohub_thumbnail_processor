import unittest

import mock

from processor import resize
from processor import resize_job


class ResizeTest(unittest.TestCase):

    def setUp(self):
        mock_pil_patch = mock.patch('processor.resize.Image.open')
        self.addCleanup(mock_pil_patch.stop)
        self.mock_pil = mock_pil_patch.start()

        self.mock_image = mock.Mock()
        self.mock_pil.return_value = self.mock_image

        self.mock_cropped_image = mock.Mock()
        self.mock_image.crop.return_value = self.mock_cropped_image

        self.mock_resized_image = mock.Mock()
        self.mock_cropped_image.resize.return_value = self.mock_resized_image

        self.mock_converted_image = mock.Mock()
        self.mock_resized_image.convert.return_value = self.mock_converted_image

    def test_resize_when_no_crop_needed(self):
        self.mock_image.size = (680, 460)

        resize.resize(resize_job.Job('large.jpg', 'small.jpg', 340, 230))

        self.mock_image.crop.assert_called_with((0, 0, 680, 460))
        self.mock_cropped_image.resize.assert_called_with((340, 230))
        self.mock_resized_image.convert.assert_called_with('RGB')
        self.mock_converted_image.save.assert_called_with('small.jpg', 'JPEG')

    def test_resize_when_horizontal_crop_is_needed(self):
        self.mock_image.size = (690, 460)

        resize.resize(resize_job.Job('large.jpg', 'small.jpg', 340, 230))

        self.mock_image.crop.assert_called_with((5, 0, 685, 460))
        self.mock_cropped_image.resize.assert_called_with((340, 230))
        self.mock_resized_image.convert.assert_called_with('RGB')
        self.mock_converted_image.save.assert_called_with('small.jpg', 'JPEG')

    def test_resize_when_vertical_crop_is_needed(self):
        self.mock_image.size = (680, 470)

        resize.resize(resize_job.Job('large.jpg', 'small.jpg', 340, 230))

        self.mock_image.crop.assert_called_with((0, 5, 680, 465))
        self.mock_cropped_image.resize.assert_called_with((340, 230))
        self.mock_resized_image.convert.assert_called_with('RGB')
        self.mock_converted_image.save.assert_called_with('small.jpg', 'JPEG')
