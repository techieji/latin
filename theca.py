import falx
from paml import AttrDict

def val_inp(prompt, validator=lambda a: True, error_msg='Invalid input.'):
    inp = falx.get_inp(prompt)
    while not validator(inp):
        print(error_msg)
        inp = falx.get_inp(prompt)
    return inp

def get_word():
    word_type = val_inp('Word type (n/v): ', lambda x: x in 'nv')
    if word_type == 'n':
        nom = val_inp('Nominative: ')
        gen = val_inp('Genitive: ')
        gender = val_inp('Gender (m/f/n): ')
        return AttrDict({
            'nom': nom,
            'gen': gen,
            'gender': gender,
        })
    elif word_type == 'v':
        pass

def get_info(word, pos):
    log = lambda a: [print(a), a][1]
    if pos == 'n':
        print()
        print('singular\tplural')
        print('--------\t------')
        for x in ['nom', 'gen', 'dat', 'acc', 'abl']:
            print(falx.decline(word.nom, word.gen, word.gender, x, 'sing'), end='\t\t'),
            print(falx.decline(word.nom, word.gen, word.gender, x, 'plur')),

get_info(get_word(), 'n')
