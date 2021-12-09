import json

class Dictionary:
    def __init__(self, d):
        self.d = d

    @staticmethod
    def from_file(filename, fail=False):
        try:
            with open(filename) as f:
                return Dictionary(json.load(f))
        except FileNotFoundError:
            if fail:
                raise
            else:
                return Dictionary({})

    def save(self, file):
        with open(
