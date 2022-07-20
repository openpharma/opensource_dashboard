import streamlit as st
from sentence_transformers import SentenceTransformer, util
import torch
import spacy
import requests

@st.cache(suppress_st_warning=True)
def read_copy_tensor():
    path_inference = 'https://openpharma.s3.us-east-2.amazonaws.com/ml/inference_description.pt'
    response = requests.get(path_inference)
    open("inference_description.pt", "wb").write(response.content)
    return 0


def clean_data(X, is_lemma: bool=True, remove_stop: bool=True, is_alphabetic: bool=True):
    """X : list of string such as ["sentence_1", "sentences_2", ... , "sentence_n"]
    Return : list of list of words 
    [
        ["word_1 word_2 ... word_n"], (sentence 1 cleaned)
        ["word_1 ... word_n"],
        .
        .
        .
        ["word_1 word_2 ... word_n"] (sentence n cleaned)
    ]
    """
    nlp = spacy.load("en_core_web_sm")
    # (is_lemma = True, remove_stop = True, is_alpha = False) = (1,1,0)
    hyperparam_tuple = (is_lemma, remove_stop, is_alphabetic)
    new_X = []
    while(True):
        if((0,0,0)==hyperparam_tuple): # everything initialize with False
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                sentence = [token.text.lower() for token in doc if(not(token.is_left_punct) and not(token.is_right_punct) and not(token.is_punct) and not(token.is_bracket))]
                new_X.append(" ".join(sentence))
            break
        elif((1,0,0)==hyperparam_tuple): # lemma_
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                sentence = [token.lemma_.lower() for token in doc if(not(token.is_left_punct) and not(token.is_right_punct) and not(token.is_punct) and not(token.is_bracket))]
                new_X.append(" ".join(sentence))
            break
        elif((0,1,0)==hyperparam_tuple): # remove stop_words
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                sentence = [token.text.lower() for token in doc if (not(token.is_stop) and not(token.is_left_punct) and not(token.is_right_punct) and not(token.is_punct) and not(token.is_bracket))]
                new_X.append(" ".join(sentence))
            break
        elif((0,0,1)==hyperparam_tuple): # only alphabetic
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                sentence = [token.text.lower() for token in doc if (token.is_alpha and not(token.is_left_punct))]
                new_X.append(" ".join(sentence))
            break
        elif((1,1,0)==hyperparam_tuple): #lemma and remove stop_words
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                sentence = [token.lemma_.lower() for token in doc if (not(token.is_stop) and not(token.is_left_punct) and not(token.is_right_punct) and not(token.is_punct) and not(token.is_bracket))]
                new_X.append(" ".join(sentence))
            break
        elif((0,1,1)==hyperparam_tuple): #remove stop_words and only alphabetic
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                sentence = [token.text.lower() for token in doc if (token.is_alpha and not(token.is_stop))]
                new_X.append(" ".join(sentence))
            break
        elif((1,0,1)==hyperparam_tuple): #lemma and only alphabetic
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                sentence = [token.lemma_.lower() for token in doc if(token.is_alpha and not(token.is_left_punct))]
                new_X.append(" ".join(sentence))
            break
        elif((1,1,1)==hyperparam_tuple): #lemma and only alphabetic and remove stop_words
            for doc in nlp.pipe(X, disable=['ner', 'parser', 'textcat']):
                sentence = [token.lemma_.lower() for token in doc if(token.is_alpha and not(token.is_stop))]
                new_X.append(" ".join(sentence))
            break
        break
    
    return new_X

class SearchEngine:
    def __init__(self):
        pass

    def read_inference(self, path: str):
        self.embed_corpus = torch.load(path)
        return self

    def fit(self, query):
        query_clean = clean_data(query, is_lemma=False, remove_stop=True, is_alphabetic=True)
        embedder = SentenceTransformer('all-MiniLM-L6-v2-BERT')
        self.embed_query = embedder.encode(query_clean, convert_to_tensor=True)
        return self

    def predict(self, topk: int=10):
        cos_scores = util.cos_sim(self.embed_query, self.embed_corpus)[0]
        top_results = torch.topk(cos_scores, k=topk)
        #Give the result with cosine similarity
        return top_results
