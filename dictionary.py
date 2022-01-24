import json
from falx import get_inp

class Dictionary(dict):
    @staticmethod
    def from_file(filename='dictionary.json', fail=False):
        try:
            with open(filename) as f:
                return Dictionary(json.load(f))
        except FileNotFoundError:
            if fail: raise
            else: return Dictionary({})

    def save(self, file='dictionary.jaon'):
        with open(file, 'w') as f:
            json.dump(self.d, f)

    def add_elem(self):
        pos = get_inp('Part of speech: ').lower()
        if pos[0] == 'v':
            l = tuple(get_inp(f'Principal part {x}' for x in range(1, 5)))
            self.d[l] = get_inp('Definition: ')
        elif pos[0] == 'n':
            l = get_inp(f'')
