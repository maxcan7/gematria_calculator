from gematria import parse_chars, calculate_gematria


# Mapping of English letter to their Hebrew letter gematria value
gematria_test_dict = {
    "A": 1,
    "B": 2,
    "G": 3,
    "D": 4,
    "H": 5,
    "E": 5,
    "U": 6,
    "V": 6,
    "W": 6,
    "Z": 7,
    "C": 8,
    "CH": 8,
    "T": 9,
    "I": 10,
    "J": 10,
    "Y": 10,
    "K": 20,
    "L": 30,
    "M": 40,
    "N": 50,
    "S": 60,
    "X": 60,
    "O": 70,
    "F": 80,
    "P": 80,
    "PH": 80,
    "TS": 90,
    "TZ": 90,
    "Q": 100,
    "R": 200,
    "SH": 300,
    "TH": 400,
    "K_FINAL": 500,
    "M_FINAL": 600,
    "N_FINAL": 700,
    "P_FINAL": 800,
    "PH_FINAL": 800,
    "TS_FINAL": 900,
    "TZ_FINAL": 900,
}


def test_parse_chars():
    """
    Tests the parsing of e.g. combos and final_words, accounting for
    differences in the English and Hebrew alphabets, and the
    Mispar gadol variant used in this calculator.
    """
    cases = {
        "a": ["A"],
        " b": ["B"],
        "c!": ["C"],
        " d": ["D"],
        "ch": ["CH"],
        "n": ["N_FINAL"],
        "ts": ["TS_FINAL"],
        "pants": ["P", "A", "N", "TS_FINAL"],
        "chutzpah": ["CH", "U", "TZ", "P", "A", "H"],
        "cherubim": ["CH", "E", "R", "U", "B", "I", "M_FINAL"],
    }
    for case in cases.keys():
        assert parse_chars(case) == cases[case]


def test_gematria_mappings():
    """
    Tests the results of the calculator against the character values
    as described on wikipedia: https://en.wikipedia.org/wiki/Gematria
    """
    for char in gematria_test_dict.keys():
        assert calculate_gematria([char]) == gematria_test_dict[char]
