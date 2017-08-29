from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
from leslie_data import get_leslie_quotes
import json

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


# get data
try:
    with open('leslie_list.json') as fp:
        leslie_quotes = json.load(fp)
except:
    leslie_quotes = get_leslie_quotes()

# clean data
doc_clean = [clean(doc).split() for doc in leslie_quotes]

# Creating the term dictionary of our corpus, unique terms assigned indexes
dictionary = corpora.Dictionary(doc_clean)

# Converting corpus into Document Term Matrix using dictionary prepared above
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=5, id2word=dictionary, passes=50)

print(ldamodel.print_topics(num_topics=5, num_words=3))
