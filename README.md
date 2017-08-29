# LeslieKnopeCompliments
Generates compliments a la Leslie Knope

`pos_compliments.py`: Uses the Datamuse API to pull common adjectives for a list of nouns that I created that seemed Leslie Knope-ish

`markov_compliments.py`: Uses a markov chain to probabilistically create sentences using a corpus of 699 Leslie Knope quotes (scraped in `leslie_data.py`)

`topic_model.py`: Uses LDA topic modeling to obtain some number k topics from the corpus of Leslie Knope quotes (scraped in `leslie_data.py` and json living in `leslie_list.json`)
