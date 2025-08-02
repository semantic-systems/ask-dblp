import torch
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json

_model = SentenceTransformer('all-MiniLM-L6-v2')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def encode_training_questions(questions, model, embed_file='train_embeddings.npy', sent_file='train_questions.json'):
    """
    Encodes and saves embeddings.
    """
    embeddings = model.encode(questions, convert_to_numpy=True)
    np.save(embed_file, embeddings)

    with open(sent_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f)
    print(f"Saved {len(questions)} embeddings to {embed_file} and sentences to {sent_file}.")


def load_embeddings(embed_file='train_embeddings.npy', sent_file='train_sentences.json'):
    """
    Loads embeddings and sentences from disk.
    """
    embeddings = np.load(embed_file)
    with open(sent_file, 'r', encoding='utf-8') as f:
        sentences = json.load(f)
    return embeddings, sentences


def identify_similar_questions(question, train_set, top_n = 1):
    pass