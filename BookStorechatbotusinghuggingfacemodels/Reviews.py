from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")

class ReviewsHandle:
    @staticmethod
    def reviews_query(query):
        inputs = tokenizer(query, return_tensors="pt")
        outputs = model(**inputs)
        probs = softmax(outputs.logits.detach().numpy()[0])
        if probs[2] > max(probs[0], probs[1]):
            response = f"You have given a positive review.{query}"
        elif probs[0] > max(probs[1], probs[2]):
            response = f"You have given a negative review.{query}"
        else:
            response = f"Emotions are mixed, so it's a neutral review.{query}"
        
        return response

