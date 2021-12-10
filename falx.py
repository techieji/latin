import paml
from dataclasses import dataclass
import re
from itertools import chain
from functools import reduce

DECL = paml.import_module('decl.paml')
CONJ = paml.import_module('conj.paml')

MACRON_DICT = {
    'i': 'ī',
    'e': 'ē',
    'a': 'ā',
    'o': 'ō',
    'u': 'ū'
}

DIPHTHONGS = ['ae', 'au', 'ei', 'eu', 'oe', 'ui']

def get_inp(p):
    return re.sub(r'.-', lambda s: MACRON_DICT[s.group(0)[0]], input(p))

def gen_to_root(gen):
    if gen.endswith('ae') or gen.endswith('is'):
        return gen[:-2]
    elif gen.endswith('ī'):
        return gen[:-1]

def find_decl(nom, gen, gender):
    if gen.endswith('ae'):
        return '1'
    elif gen.endswith('ī'):
        return '2n' if gender == 'n' else '2'
    elif gen.endswith('is'):
        if is_strong_i_stem(nom, gen, gender):
            return '3I'
        elif is_weak_i_stem(nom, gen):
            return '3i'
        elif gender == 'n':
            return '3n'
        else:
            return '3'

def decline(nom, gen, gender, form: str, num):
    return DECL.get_form(find_decl(nom, gen, gender), form, num).replace('!', nom).replace('%', gen_to_root(gen))

def find_conj(p2):
    c = p2[-3]
    if c == 'ā':
        return '1'
    elif c == 'ē':
        return '2'
    elif c == 'e':
        return '3' if p2[-2:] != 'io' else '3io'
    elif c == 'i':
        return '4'

def inf_to_root(p2):
    return p2[:-3]

def conjugate(p1, p2, p3, p4, tense, person, number):
    return CONJ.get_form(tense, find_conj(p2), number, person).replace('1', p1).replace('%', inf_to_root(p2))

def count_syllables(s):
    a = reduce(lambda s, a: s.replace(a, '!'), DIPHTHONGS)
    return sum(map(a.count, chain(MACRON_DICT.keys(), MACRON_DICT.values(), '!')))

def is_weak_i_stem(nom, gen):
    if nom in ['canis']: return False   # Move to data file
    return (nom[-2:] in ['is', 'ēs'] and count_syllables(nom) == count_syllables(gen)) or (count_syllables(nom) == 1 and nom[-1] in ['s', 'x'] and gen_to_root(gen)[-2] in CONSONANTS and gen_to_root(gen)[-1] in CONSONANTS)

def is_strong_i_stem(nom, gen, gender):
    return gender == 'n' and any(map(nom.endswith, ['e', 'al', 'ar']))

if __name__ == '__main__':
    # print(decline(get_inp('nom: '), get_inp('gen: '), get_inp('gdr: '), get_inp('frm: '), get_inp('num: ')))
    # print(decline('mare', 'maris', 'n', 'acc', 'plur'))
    print(conjugate('teneo', 'tenēre', '', '', 'present', '1', 'plur'))
