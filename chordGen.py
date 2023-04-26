import random

# Building blocks of the most common chord notations
SimpleChordNames = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'F', 'F#', 'G', 'Ab']
# TODO in case of change in SimpleChordTypes check function build_chord
SimpleChordTypes = ['Dim', 'm', 'm', '', '']
SimpleDimSevenths = ['7']
SimpleMinorSevenths = ['7b5', '7']
SimpleMajorSevenths = ['7', 'Maj7']

# Building every possible chord name basic blocks
ChordLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Accidentals = ['', 'b', '#']
# Building blocks of the  most common chord types
ChordTypes = ['Dim', 'm', '', '+']
SeventhChordTypes = ['7-', '7', 'Maj7']

ChordNames = []
for ChordLetter in ChordLetters:
    for Accident in Accidentals:
        EnharmonicChord = ChordLetter + Accident
        # remove 4 secretly evil accidentals
        if EnharmonicChord not in ['B#', 'Cb', 'E#', 'Fb']:
            ChordNames.append(EnharmonicChord)


def get_random_element(array):
    selected_random_value = random.randint(0, len(array) - 1)
    return array[selected_random_value]


def build_chord(is_simple: bool, is_seventh: bool):
    """
    IMPORTANT!
    Compares against values in SimpleChordTypes as string
    Do not change strings in this list
    :param is_simple:
    :param is_seventh:
    :return: chord based on user preference
    """

    chord_name = get_random_element(ChordNames)
    chord_type = get_random_element(ChordTypes)
    chord_seventh = ""
# Only chord_seventh might be empty

    if is_simple:
        chord_name = get_random_element(SimpleChordNames)
        chord_type = get_random_element(SimpleChordTypes)

    if is_seventh and is_simple:
        match chord_type:
            case 'Dim':
                chord_seventh = get_random_element(SimpleDimSevenths)
            case 'm':
                chord_seventh = get_random_element(SimpleMinorSevenths)
            case _:
                chord_seventh = get_random_element(SimpleMajorSevenths)

    if is_seventh and not is_simple:
        chord_seventh = get_random_element(SeventhChordTypes)

    return chord_name + chord_type + chord_seventh
