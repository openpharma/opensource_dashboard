import streamlit as st
from sentence_transformers import SentenceTransformer, util
import torch
import requests

@st.cache(suppress_st_warning=True, ttl=43200)
def read_copy_tensor_packages():
    path_inference = 'https://openpharma.s3.us-east-2.amazonaws.com/ml/inference_packages.pt'
    response = requests.get(path_inference)
    open("inference_packages.pt", "wb").write(response.content)
    embed_corpus = torch.load("inference_packages.pt")
    return embed_corpus

@st.cache(suppress_st_warning=True, ttl=43200)
def read_copy_tensor_openissues():
    path_inference = 'https://openpharma.s3.us-east-2.amazonaws.com/ml/inference_openissues.pt'
    response = requests.get(path_inference)
    open("inference_openissues.pt", "wb").write(response.content)
    embed_corpus = torch.load("inference_openissues.pt")
    return embed_corpus


class SearchEngine:
    def __init__(self, embed_corpus):
        self.embed_corpus = embed_corpus

    def fit(self, query):
        print(query)
        query = query.lower()
        embedder = SentenceTransformer('LM-L6-BERT')
        self.embed_query = embedder.encode(query, convert_to_tensor=True)
        return self

    def predict(self, topk: int=10):
        cos_scores = util.cos_sim(self.embed_query, self.embed_corpus)[0]
        top_results = torch.topk(cos_scores, k=topk)
        #Give the result with cosine similarity
        return top_results
