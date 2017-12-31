import json


class Job(object):

    def __init__(self, raw_path, resized_path, new_width, new_height):
        self._raw_path = raw_path
        self._resized_path = resized_path
        self._new_width = new_width
        self._new_height = new_height

    def raw_path(self):
        return self._raw_path

    def resized_path(self):
        return self._resized_path

    def new_width(self):
        return self._new_width

    def new_height(self):
        return self._new_height

    def __eq__(self, other):
        return ((self.raw_path() == other.raw_path()) and
                (self.resized_path() == other.resized_path()) and
                (self.new_width() == other.new_width()) and
                (self.new_height() == other.new_height()))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return json.dumps({
            'raw_path': self.raw_path(),
            'resized_path': self.resized_path(),
            'new_width': self.new_width(),
            'new_height': self.new_height(),
        })
