import unittest

from processor import supported_file


class SupportedFileTest(unittest.TestCase):

    def test_recognizes_supported_files(self):
        self.assertTrue(supported_file.is_supported('/foo/original-a.jpg'))
        self.assertTrue(supported_file.is_supported('/foo/original-a.jpeg'))
        self.assertTrue(supported_file.is_supported('/foo/original-a.JPG'))
        self.assertTrue(supported_file.is_supported('/foo/original-a.JPEG'))
        self.assertTrue(supported_file.is_supported('/foo/original-a.png'))
        self.assertTrue(supported_file.is_supported('/foo/original-a.PNG'))

        self.assertFalse(supported_file.is_supported('/foo/Thumbs.db'))
        self.assertFalse(supported_file.is_supported('Thumbs.png.notanimage'))
        self.assertFalse(supported_file.is_supported('/foo/.png'))
        self.assertFalse(supported_file.is_supported('/foo/bar'))
        self.assertFalse(supported_file.is_supported('/foo/bar/'))
        self.assertFalse(supported_file.is_supported('/foo/png'))
