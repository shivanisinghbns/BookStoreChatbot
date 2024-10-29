import spacy
from textblob import TextBlob
nlp = spacy.load("en_core_web_sm")
class ReviewsHandle:
    def reviews_query(query):
        blob = TextBlob(query)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            response = "You have given a positive review."
        elif sentiment < 0:
            response = "You have given a negative review."
        else:
            response = "Emotions are mixed, so it's a neutral review."

        return response