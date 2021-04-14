from collections import defaultdict, Counter
from nltk import word_tokenize
from nltk.corpus import words, stopwords
from .LyricsDB import LyricsDB as LDB
import pickle
import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'genius28k.p')

df= pickle.load(open(filename, 'rb'))
db = LDB(df)
db.fit()

def search_back_fn(query):
    return(db.cosine_sim_rank(query))
