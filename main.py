import itertools

"""
    TODO:
        - Currently only 7 strings guitar and 5 strings bass max for setting tuning from base
"""

notes_translation = {
    'A': 'La',
    'B': 'Si',
    'C': 'Do',
    'D': 'Re',
    'E': 'Mi',
    'F': 'Fa',
    'G': 'Sol'
}

mod_notes = list(itertools.chain.from_iterable((str(k), str(v)) for (k, v) in notes_translation.items() if k != 'B' and k != 'E'))

class Instrument:
    def __init__(self, name, nb_more_strings=0):
        self.name = name
        self.nb_more_strings = nb_more_strings

class Note:
    def __init__(self, name):
        self.name = name

        self.possible_mod = []
        self.half_tone = 1

        if name in mod_notes:
            self.possible_mod = ['#', 'b']
            self.half_tone = 2

    def print_note(self, display_lang='en'):
        sstr = ''
        if display_lang == 'fr':
            sstr += f"{notes_translation[self.name]}"
        else:
            sstr += f"{self.name}"
        
        if display_lang == 'fr' and self.name == 'G':
            sstr += f" ({self.half_tone})"

        else:
            sstr += f"  ({self.half_tone})"

        print(sstr)
            

    def __str__(self):
        sstr = f'{self.name} ({self.half_tone})'

        return sstr

        

class Tuning:
    def __init__(self, instrument, base=''):
        self.notes = []
        self.instrument = instrument
        self.set_tuning_from_base(base)

    def set_tuning_from_base(self, base):
        # default (B)EADG[BE]
        if not base:
            if self.instrument.nb_more_strings > 0:
                self.notes.append(Note('B'))

            self.notes.append(Note('E'))
            self.notes.append(Note('A'))
            self.notes.append(Note('D'))
            self.notes.append(Note('G'))
            self.notes.append(Note('B'))
            self.notes.append(Note('E'))

    def print_notes(self, display_lang='en'):
        for note in self.notes:
            note.print_note(display_lang)

            

def main():
    tun = Tuning(Instrument('Guitar'))
    tun.print_notes('fr')

if __name__ == "__main__":
    main()