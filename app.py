import random

SimpleChordNames = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'F', 'F#', 'G', 'Ab']
SimpleChordTypes = ['Dim', 'm', '', '+', 'Dim7-', '7b5', 'm7', 'mMaj7', '7', 'Maj7']

def print_random_simple_chord():
    random_simple_chord_number = random.randint(0, len(SimpleChordNames) - 1)
    random_simple_chord_type_number = random.randint(0, len(SimpleChordTypes) - 1)
    print(
      SimpleChordNames[random_simple_chord_number]
        + SimpleChordTypes[random_simple_chord_type_number])


# Building chord name basic blocks
ChordLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Accidentals = ['', 'b', '#']
EvilAccidentals = ['', 'b', 'bb', '#', '##']

# Chord Name lists - one normal and one evil
EnharmonicChords = []
for ChordLetter in ChordLetters:
    for accident in Accidentals:
        EnharmonicChord = ChordLetter + accident
        EnharmonicChords.append(EnharmonicChord)


EvilEnharmonicChords = []
for ChordLetter in ChordLetters:
    for EvilAccident in EvilAccidentals:
        EvilEnharmonicChord = ChordLetter + EvilAccident
        EvilEnharmonicChords.append(EvilEnharmonicChord)


ChordTypes = ['Dim', 'm', '', '+']
SeptaChordTypes = ['7-', '7', 'Maj7', '']
# I placed the empty string in SeptaChordSigns in order to generate regular chords but there must be a better way
# There should be another list with chords other than 7ths - 6, 9b, sus2, etc.
# Maybe even other chord types - like quartal

Used_ChordNames = EnharmonicChords
Used_ChordTypes = ChordTypes
Used_SeptaChordTypes = SeptaChordTypes


def print_random_chord():
    random_chord_number = random.randint(0, len(Used_ChordNames) - 1)
    random_chord_type_number = random.randint(0, len(Used_ChordTypes) - 1)
    random_septachord_name_number = random.randint(0, len(Used_SeptaChordTypes) - 1)

    print(
        Used_ChordNames[random_chord_number]
        + Used_ChordTypes[random_chord_type_number]
        + SeptaChordTypes[random_septachord_name_number])


print_random_simple_chord()
