import re
from Order import Order_handle
from Reviews import ReviewsHandle
from StorePolicy import Store_handle
import json
from Book import Bookhandle
from transformers import pipeline
class main_handle:
    def __init__(self,user_query):
        self.user_query=user_query
        with open('books.json', 'r') as books_file:
            self.books_data = json.load(books_file)
        self.classifier=pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
        self.lables=["Book query", "Review about the book", "Store policy", "order related query"]
        self.reponse=self.hadle_query()
    def hadle_query(self):
        query=self.user_query
        books=self.books_data
        classifier=self.classifier
        candidate_labels=self.lables
        output = classifier(query, candidate_labels, multi_label=False)
        print(output['labels'][0])
        if output['labels'][0]=="order related query" or re.search(r'\b[A-Za-z]\d{3}\b', query) :
            response=Order_handle.Order_query(query)
            return response
        elif output['labels'][0]=="Review about the book":
            response=ReviewsHandle.reviews_query(query)
            return response
        elif output['labels'][0]=="Store policy":
            response=Store_handle.storepolicy_query(query)
            return response
        elif output['labels'][0]=="Book query":
            response=Bookhandle.book_query(query,books)
            return response
        else:
            response="Please clarify your query are you asking aout order,book,store policy or giving review."
            return response
         


    