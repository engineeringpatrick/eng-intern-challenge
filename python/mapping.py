CHAR_TO_BRAILLE = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    ' ': "......",
}

DIGIT_TO_BRAILLE = {
	'1': "O.....",
	'2': "O.O...",
	'3': "OO....",
	'4': "OO.O..",
	'5': "O..O..",
	'6': "OOO...",
	'7': "OOOO..",
	'8': "O.OO..",
	'9': ".OO...",
	'0': ".OOO..",
}

CAPITAL_FOLLOWS_TOKEN = '.....O'
NUMBER_FOLLOWS_TOKEN = '.O.OOO'

BRAILLE_TO_CHAR = {v: k for k, v in CHAR_TO_BRAILLE.items()}
BRAILLE_TO_DIGIT = {v: k for k, v in DIGIT_TO_BRAILLE.items()}

VALID_BRAILLE_TOKENS = list(CHAR_TO_BRAILLE.values()) + list(DIGIT_TO_BRAILLE.values()) + [CAPITAL_FOLLOWS_TOKEN] + [NUMBER_FOLLOWS_TOKEN]