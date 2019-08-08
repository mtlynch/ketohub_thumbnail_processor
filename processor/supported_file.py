import os

_SUPPORTED_EXTENSIONS = set(['.jpg', '.jpeg', '.png', '.webp'])


def is_supported(path):
    extension = os.path.splitext(path)[1]
    return extension.lower() in _SUPPORTED_EXTENSIONS
