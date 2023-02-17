import sys
import re
from typing import List, Tuple
from math import floor


# Accounting for Hebrew characters that don't have equivalents
# in Latin characters or the English language.
combo_list_start = ["C", "P", "T", "S"]
combo_list_end = ["H", "S", "Z"]
finals_dict = {
    "K": "K_FINAL",
    "M": "M_FINAL",
    "N": "N_FINAL",
    "P": "P_FINAL",
    "PH": "PH_FINAL",
    "TS": "TS_FINAL",
    "TZ": "TZ_FINAL",
}

# Mapping from Latin characters to their Hebrew character index
# i.e. A == Aleph == 1, CH == HET == 8
char_idx_mappings = {
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
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "S": 15,
    "X": 15,
    "O": 16,
    "F": 17,
    "P": 17,
    "PH": 17,
    "TS": 18,
    "TZ": 18,
    "Q": 19,
    "R": 20,
    "SH": 21,
    "TH": 22,
    "K_FINAL": 23,
    "M_FINAL": 24,
    "N_FINAL": 25,
    "P_FINAL": 26,
    "PH_FINAL": 26,
    "TS_FINAL": 27,
    "TZ_FINAL": 27,
}


def calculate_gematria(chars: List[str]) -> int:
    """
    Run the Gematria Cipher by calculating the Gematria value of each
    character and returning the sum of all values.
    """
    return sum(
        [
            10 ** floor((char_idx_mappings[x] - 1) / 9)
            * (((char_idx_mappings[x] - 1) % 9) + 1)
            for x in chars
        ]
    )


def add_finals_chars(chars: List[str]) -> List[str]:
    """
    If a character is the final character in the word and has a unique
    Mispar gadol variant, swap the character for its FINAL variant.
    """
    if chars[-1] in finals_dict.keys():
        chars[-1] = finals_dict[chars[-1]]
    return chars


def build_combo_chars(
    chars: List[str], combo_indices: List[Tuple[int, int]]
) -> List[str]:
    """
    For all combos, concatenate those characters in the chars list.
    """
    for combo in combo_indices:
        chars[combo[0]] = chars[combo[0]] + chars[combo[1]]
    drop_combo_ends = [x[1] for x in combo_indices]
    chars = [x for i, x in enumerate(chars) if i not in drop_combo_ends]
    return chars


def find_combos(chars: List[str]) -> List[Tuple[int, int]]:
    """
    Find characters in the word which correspond to Hebrew characters with no
    English equivalents.
    Returns a list of tuples, where each tuple has the start and end index
    of the combo in the chars list.
    """
    if len(chars) == 1:
        return []
    if len(chars) == 2:
        if chars[1] in combo_list_end and chars[0] in combo_list_start:
            return [(0, 1)]
    prev_char = chars[0]
    combo_indices = []
    for i, char in enumerate(chars[1:]):
        if char in combo_list_end and prev_char in combo_list_start:
            combo_indices.append((i, i + 1))
        prev_char = chars[i + 1]
    return combo_indices


def parse_chars(word: str) -> List[str]:
    """
    Parse non-chars and make words upper, split the word string into a
    list of characters, find combos or finals, etc., for calculating
    gematria.
    """
    word = re.compile("[^a-zA-Z]").sub("", word).upper()
    chars = [*word]
    combo_indices = find_combos(chars)
    chars = build_combo_chars(chars, combo_indices)
    chars = add_finals_chars(chars)
    return chars


def main(word: str) -> int:
    chars = parse_chars(word)
    print(f"{word} was parsed as {chars}")
    gematria = calculate_gematria(chars)
    print(f"gematria value is {gematria}")


if __name__ == "__main__":
    main(sys.argv[1])
