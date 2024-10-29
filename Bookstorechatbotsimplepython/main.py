import re
from Order import Order_handle
from Reviews import ReviewsHandle
from StorePolicy import Store_handle
import json
from Book import Bookhandle
class main_handle:
    def __init__(self,user_query):
        self.user_query=user_query
        with open('reviews.json', 'r') as reviews_file:
            self.reviews_data = json.load(reviews_file)
        with open('books.json', 'r') as books_file:
            self.books_data = json.load(books_file)
        with open('storepolicy.json', 'r') as books_file:
            self.storepolicy = json.load(books_file)
        self.reponse=self.hadle_query()
    def hadle_query(self):
        query=self.user_query
        reviews_corpora=self.reviews_data
        books=self.books_data
        storepolicy=self.storepolicy
        if 'order' in query.lower() or 'status' in query.lower() or 'delivery' in query.lower() or re.search(r'\b[A-Za-z]\d{3}\b', query) :
            response=Order_handle.Order_query(query)
            return response
        elif any(word.lower() in query.lower() for word in reviews_corpora['positive_words']) or any(word.lower() in query.lower() for word in reviews_corpora['negative_words']):
            response=ReviewsHandle.reviews_query(query)
            return response
        elif 'policy' in query.lower() or any(word.lower() in query.lower() for word in storepolicy['store_policy_keywords']):
            response=Store_handle.storepolicy_query(query)
            return response
        elif 'thank you' in query.lower() or 'bye' in query.lower() or len(query.split(' '))<=2:
            response="Have a nice day! Thanks for visit."
            return response
        else:
            response=Bookhandle.book_query(query,books)
            return response
         



    