import paml
from dataclasses import dataclass

DECL = paml.import_module('decl.paml')

@dataclass
class Noun:
    nom: str
    gen: str
    conj: int
    _root: type(None)

    @property
    def root(self):
        if _root:
            return _root
        else:
            return nom[:-1] if conj == 2 else nom[:-2]

def decline(noun: Noun, decl: str, form: str, num: str):
    return getattr(getattr(getattr(DECL, decl), num), form).replace("!", noun.nom).replace("%", noun.root)
