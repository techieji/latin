import paml
from dataclasses import dataclass
import re

DECL = paml.import_module('decl.paml')

MACRON_DICT = {
    'i': 'ī',
    'e': 'ē',
    'a': 'ā',
    'o': 'ō'     # TODO: Finish!
}

def get_inp(p):
    return re.sub(r'.-', lambda s: MACRON_DICT[s.group(0)[0]], input(p))

def gen_to_root(gen):
    if gen.endswith('ae') or gen.endswith('is'):
        return gen[:-2]
    elif gen.endswith('ī'):
        return gen[:-1]

def find_decl(nom, gen):
    if gen.endswith('ae'):
        return '1'
    elif gen.endswith('ī'):
        return '2n' if nom[-1] == 'm' else '2'
    elif gen.endswith('is'):
        return '3'

def decline(nom, gen, form: str, num):
    return DECL.get_form(find_decl(nom, gen), form, num).replace('!', nom).replace('%', gen_to_root(gen))

def count_syllables(s):
    a = s.replace('ae', '!').replace('oe', '!')    # replaces dipthongs
    n = 0
    for x in ['a', 'e', 'i', 'o', 'u', '!']:
        n += a.count(x)
    return n

def is_weak_i_stem(nom, gen):
    return (nom[-2:] in ['is', ''])

# print(decline(get_inp('nom: '), get_inp('gen: '), get_inp('form: '), get_inp('num: ')))

print(count_syllables(get_inp('asdf: ')))
