# Gematria Calculator

## What is this?
This script calculates the Gematria value of words.
It uses the Mispar gadol cipher, a variant on the standard encoding
where certain letters at the end of the word have a different value.

Popular Gematria calculators online often assume English character indices
even when nominally being "Hebrew" calculators. This calculator maps
the Latin characters of the English alphabet to their closest Hebrew
equivalent.

The unit tests in gematria_test.py demonstrate the efficacy of the
Gematria value mappings of these characters, and the char_idx_mappings show
the index mappings.

https://en.wikipedia.org/wiki/Gematria


## What is Gematria?
Gematria is a kind of Numerology in Jewish Mysticism. It's basically just an interpretive thing not unlike I Ching or Tarot, but what I find particularly interesting about it is that there is an actual algorithm you can work with.

Of course any meaning you derive is going to be of an interpretive, personal, symbolic, etc. nature, but it can be operationalized quantitatively and used to produce reliable results, and I just find that really interesting; it's like divinatory math poetry.


## How to use
From whatever directory you've saved this repo, run:

python gematria.py 'word'

Where 'word' is any word you'd like to calculate.


## Future Developments
This could be expanded to support more ciphers or non-Latin characters.
