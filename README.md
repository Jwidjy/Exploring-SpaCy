# Exploring-SpaCy
First foray into NLP with spaCy using the `en_core_web_md` language model. `semantics.py` involves testing with vectors and short text. `watch_next.py` is a system that will tell you what to watch next based on word vector similarity of the description of movies.

## Install
- `pip3 install spacy`
- `en_core_web_md`

## Usage
For `semantics.py`, after the relevant components have been installed, run:
```
$ python semantics.py
```
This script will output similarity float values ranging from 0 to 1, with 0 being the most dissimilar, with the strength of the similarity increasing all the way up to 1.

For `watch_next.py`, after the relevant components have been installed, run:
```
$ python watch_next.py
```
This script will output what movie to watch next, based on a given description. It will compare this description to a list of movie descriptions in `movies.txt`, calculate similarity values, & return the movie with the highest similarity value.
