import os
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import utils
import warnings
warnings.filterwarnings("ignore", message="`encoder_attention_mask` is deprecated")

train_set = utils.load_json_data("data/train/questions.json")
train_set_list = train_set.get('questions')
training_data = [(item["id"], utils.get_value_from_dict(item["paraphrased_question"], "string")) for item in
                 train_set_list]

qid_with_entities = utils.load_json_data("data/train/train_qid_with_entities.json")
qid_with_sparql = utils.load_json_data("data/train/train_qid_with_sparql.json")
# train_set = utils.load_json_data("experiment/ask-dblp/train_data.json")
# training_data = [(item["id"], item["formal_question"]) for item in train_set]
#
# qid_with_entities = {item["id"]:item["entities"] for item in train_set}
# qid_with_sparql = {item["id"]:item["sparql"] for item in train_set}

class QuestionSimilarityIdentifier:
    def __init__(self, model_name='all-MiniLM-L6-v2', model_save_path='qsim_model_ask_dblp'):
        """
        Initialize or load existing model and data.

        Args:
          model_name: pretrained model name to use
          model_save_path: folder path for saving/loading model and data
        """
        self.model_name = model_name
        self.model_save_path = model_save_path

        self.model = None
        self.train_question_ids = []
        self.train_questions = []
        self.train_question_embeddings = None

        if self._check_saved_model():
            self._load()
        else:
            # no saved model yet, will require fitting
            print("No saved model found. Please train with fit().")

    def _check_saved_model(self):
        model_dir_exists = os.path.isdir(self.model_save_path)
        data_file_exists = os.path.isfile(os.path.join(self.model_save_path, 'data.pkl'))
        return model_dir_exists and data_file_exists

    def fit(self, questions_with_ids):
        """
        Fit/encode questions and save model and embeddings.

        Args:
          questions_with_ids: list of tuples (id, question)
        """
        print(f"Training/fitting with {len(questions_with_ids)} questions...")
        self.model = SentenceTransformer(self.model_name)

        self.train_question_ids = [qid for qid, _ in questions_with_ids]
        self.train_questions = [q for _, q in questions_with_ids]

        self.train_question_embeddings = self.model.encode(self.train_questions, convert_to_tensor=True)

        # Save model and data
        os.makedirs(self.model_save_path, exist_ok=True)
        self.model.save(self.model_save_path)

        data_to_save = {
            'question_ids': self.train_question_ids,
            'questions': self.train_questions,
            'embeddings': self.train_question_embeddings.cpu()
        }
        with open(os.path.join(self.model_save_path, 'data.pkl'), 'wb') as f:
            pickle.dump(data_to_save, f)

        print(f"Model and data saved to '{self.model_save_path}'.")

    def _load(self):
        """
            Load model and data if not already loaded or trained.
            """
        if self.model is None:
            model_path = self.model_save_path
            if os.path.isdir(model_path):
                print(f"Loading model from {model_path}...")
                self.model = SentenceTransformer(model_path)
            else:
                print("Model directory not found. Skipping model load.")
        data_path = os.path.join(self.model_save_path, 'data.pkl')
        if os.path.isfile(data_path):
            print(f"Loading data from {data_path}...")
            with open(data_path, 'rb') as f:
                data = pickle.load(f)
            self.train_question_ids = data['question_ids']
            self.train_questions = data['questions']
            self.train_question_embeddings = data['embeddings']
            print("Data loaded successfully.")
        else:
            print("Data file not found. Skipping data load.")

    def find_similar(self, new_question, top_k=7, threshold=0.6):
        """
        Find top-k most similar questions to the new question.

        Args:
          new_question: str
          top_k: int, max number of similar questions to return
          threshold: float, similarity threshold

        Returns:
          List of tuples (id, question, similarity_score)
        """
        # if self.model is None or self.train_question_embeddings is None:
        #     raise ValueError("Model or embeddings not loaded. Please fit the model first.")

        new_emb = self.model.encode([new_question], convert_to_tensor=True)

        new_emb_np = new_emb.cpu().numpy()
        train_emb_np = self.train_question_embeddings.cpu().numpy()

        cos_scores = cosine_similarity(new_emb_np, train_emb_np)[0]

        indices = np.argsort(-cos_scores)

        results = []
        for idx in indices:
            score = float(cos_scores[idx])
            if score < threshold:
                break
            results.append((self.train_question_ids[idx], self.train_questions[idx], score))
            if len(results) >= top_k:
                break

        return results

    def update_if_new_data(self, new_questions_with_ids):
        """
        Check if there are new questions (by IDs) compared to saved dataset.
        If new questions exist, refit model with combined questions and save.

        Args:
          new_questions_with_ids: list of (id, question)

        Returns:
          bool: True if model was updated, False otherwise
        """
        new_ids = {qid for qid, _ in new_questions_with_ids}
        existing_ids = set(self.train_question_ids)

        unseen_ids = new_ids - existing_ids
        if not unseen_ids:
            print("No new questions detected. Skipping retraining.")
            return False

        print(f"New questions detected: {len(unseen_ids)}. Retraining model...")

        # Combine old and new questions, avoid duplicates
        combined_dict = {qid: q for qid, q in zip(self.train_question_ids, self.train_questions)}
        combined_dict.update({qid: q for qid, q in new_questions_with_ids})

        combined_questions_with_ids = list(combined_dict.items())

        self.fit(combined_questions_with_ids)
        return True


def identify_similar_questions(qsim, question):
    results = qsim.find_similar(question, top_k=7, threshold=0.6)
    results_with_sparql = []
    if results:
        for qids, qu, score in results:
            results_with_sparql.append((qids, qu, score, qid_with_sparql[qids], qid_with_entities[qids]))
        return results_with_sparql
    return []


def prepare_data_for_training():
    qid_with_sparql = {item2["id"]: utils.get_value_from_dict(item2["query"], "sparql") for item2 in train_set}
    qid_with_entities =  {item3["id"]: item3["entities"] for item3 in train_set}
    utils.write_to_json(qid_with_sparql,"experiment/train_qid_with_sparql.json")
    utils.write_to_json(qid_with_entities, "experiment/train_qid_with_entities.json")

def main():
    qsim = QuestionSimilarityIdentifier()

    # Train if needed (no saved model)
    if qsim.model is None:
        qsim.fit(training_data)

    # Query similar questions
    query_question = "Who are the authors of Ways to study Python programming?"
    results = qsim.find_similar(query_question, top_k=3, threshold=0.3)
    print("Similar questions found:")
    for qid, question, score in results:
        print(f"ID: {qid} | Score: {score:.3f} | Question: {question}")
    # Add some new questions and retrain if they are new
    # existing, won't retrain
    # new_data = [
    #     ("id003", "What is the first paper Hannah Bast publishes?"),
    #     ("id007", "When was the Python tutorials for beginners book published?"),
    #     ("id005", "Recent papers on machine learning from WWW."),
    # ]
    # updated = qsim.update_if_new_data(new_data)
    # print("Model updated:" if updated else "No update performed.")
    #
    # # Now test again after update
    # results = qsim.find_similar(query_question, top_k=3, threshold=0.5)
    # print("\nSimilar questions after update:")
    # for qid, question, score in results:
    #     print(f"ID: {qid} | Score: {score:.3f} | Question: {question}")


if __name__ == '__main__':
    main()
    # prepare_data_for_training()