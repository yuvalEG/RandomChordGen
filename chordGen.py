import random

# Building blocks of the most common chord notations
SimpleChordNames = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'F', 'F#', 'G', 'Ab']
# TODO in case of change in SimpleChordTypes check function build_chord
SimpleChordTypes = ['Dim', 'm', '']
SimpleSeventhChordTypes = ['7b5', 'm7', '7', 'Maj7']
SimpleDimSeventh = ['m7', '7']
SimpleMinorSeventh = ['7b5', '7']

# Building every possible chord name basic blocks
ChordLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Accidentals = ['', 'b', '#']
# Building blocks of the  most common chord types
ChordTypes = ['Dim', 'm', '', '+']
SeventhChordTypes = ['7-', '7', 'Maj7']

"""
There should be another list with chords other than 7ths - 6, 9b, sus2, etc.
Maybe even other basic chord types - like quartal
"""

ChordNames = []
for ChordLetter in ChordLetters:
    for Accident in Accidentals:
        EnharmonicChord = ChordLetter + Accident
        # remove 4 secretly evil accidentals
        if EnharmonicChord != 'B#' or 'Cb' or 'E#' or 'Fb':
            ChordNames.append(EnharmonicChord)
'''
# Building a list with Double Accidentals
EvilAccidentals = ['', 'b', 'bb', '#', '##']
EvilEnharmonicChordNames = []
for ChordLetter in ChordLetters:
    for EvilAccident in EvilAccidentals:
        EvilEnharmonicChord = ChordLetter + EvilAccident
        EvilEnharmonicChordNames.append(EvilEnharmonicChord)
'''


def get_random_element(array):
    selected_random_value = random.randint(0, len(array) - 1)
    return array[selected_random_value]


def build_chord(isSimple:bool, isSeventh:bool):
    """
    :param isSimple:
    :param isSeventh:
    :return: chord based on user preference
    IMPORTANT!
    Compares against values in SimpleChordTypes as string
    Do not change 'Dim' and 'm'
    """

    chordName = ""
    chordType = ""
    chordSeventh = ""

    if isSimple:
        chordName = get_random_element(SimpleChordNames)
        chordType = get_random_element(SimpleChordTypes)

    else:
        chordName = get_random_element(ChordNames)
        chordType = get_random_element(ChordTypes)


    if isSeventh and isSimple:
        match chordType:
            case 'Dim':
                chordSeventh = get_random_element(SimpleDimSeventh)
            case 'm':
                chordSeventh = get_random_element(SimpleMinorSeventh)
            case _:
                chordSeventh = get_random_element(SimpleSeventhChordTypes)


    if isSeventh and not isSimple:
        chordSeventh = get_random_element(SeventhChordTypes)

    return chordName+chordType+chordSeventh


'''
    if isSeventh:
        if simplify_checker.get():
            used_seventh_chords = chordGen.SimpleSeventhChordTypes
        else:
            used_seventh_chords = chordGen.SeventhChordTypes
'''

