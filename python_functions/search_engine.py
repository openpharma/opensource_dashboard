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
    embed_corpus = torch.load("inference_description.pt")
    return embed_corpus


class SearchEngine:
    def __init__(self, embed_corpus):
        self.embed_corpus = embed_corpus

    def fit(self, query):
        query = query.lower()
        embedder = SentenceTransformer('LM-L6-BERT')
        self.embed_query = embedder.encode(query, convert_to_tensor=True)
        return self

    def predict(self, topk: int=10):
        cos_scores = util.cos_sim(self.embed_query, self.embed_corpus)[0]
        top_results = torch.topk(cos_scores, k=topk)
        #Give the result with cosine similarity
        return top_results
