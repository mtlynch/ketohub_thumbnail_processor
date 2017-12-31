import logging

from PIL import Image

logger = logging.getLogger(__name__)


def resize(resize_job):
    image = Image.open(resize_job.raw_path())
    x, y = image.size
    aspect_ratio = float(resize_job.new_width()) / float(
        resize_job.new_height())
    if (float(x) / float(y)) >= aspect_ratio:
        delta = x - (aspect_ratio * float(y))
        borders = (int(delta / 2), 0, int(x - (delta / 2)), y)
    else:
        delta = y - ((1.0 / aspect_ratio) * float(x))
        borders = (0, int(delta / 2), x, int(y - (delta / 2)))
    image = image.crop(borders)
    image = image.resize((resize_job.new_width(), resize_job.new_height()))
    image = image.convert("RGB")
    image.save(resize_job.resized_path(), 'JPEG')
