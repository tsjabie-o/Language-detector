# Language detector
Assignment for the _Computational Linguistics_ course

This program guesses what language a text is written in.
There is a database of texts and their languages included. This database is divided up in a training set and a test set. `write_profiles.py` uses the training set to create a directory of models (already included in repo) with all *n-grams* (*bi- and trigrams*) of the training set corpus.
These models are used by `matchlang.py` to create language profiles. These profiles are then used to compare the texts in the test set against. The language with the highest score will be the guess for that text. All of the linguistic logic is done in `langdetect.py`, it uses n-grams and cosine-similarity.
