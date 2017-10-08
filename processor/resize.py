import logging

from PIL import Image

logger = logging.getLogger(__name__)

THUMBNAIL_WIDTH = 340
THUMBNAIL_HEIGHT = 230
THUMBNAIL_RATIO = float(THUMBNAIL_WIDTH) / float(THUMBNAIL_HEIGHT)


def resize(image_path, resized_path):
    image = Image.open(image_path)
    x, y = image.size
    if (float(x) / float(y)) >= THUMBNAIL_RATIO:
        delta = x - (THUMBNAIL_RATIO * float(y))
        borders = (int(delta / 2), 0, int(x - (delta / 2)), y)
    else:
        delta = y - ((1.0 / THUMBNAIL_RATIO) * float(x))
        borders = (0, int(delta / 2), x, int(y - (delta / 2)))
    image = image.crop(borders)
    image = image.resize((THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
    image.save(resized_path, 'JPEG')
