import json
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)
from langchain.schema import SystemMessage
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] =os.getenv("API_KEY")

class main_handle:
    def __init__(self,user_query):
        self.user_query=user_query
        with open('books.json', 'r') as books_file:
            self.books_data = json.load(books_file)
        self.reponse=self.hadle_query()
    def hadle_query(self):
        query=self.user_query
        books=self.books_data
        prompt = ChatPromptTemplate.from_messages([SystemMessage(content=f"""SystemMessage: You are a bookstore chatbot specialized in understanding and responding to user needs based on their input. Users may ask about store policies, provide a review of a book, inquire about an order, or ask about a specific book.

Available Data:
Book Data: {books} (You have access only to this data; respond using only this information.Find the closest match to the book title extracted from the message.)
User can ask about the book with there author name, title or the published date or year all present in Book Data. 
Order ID Format: A fixed format with 1 alphabet followed by 3 numbers.(For ex: A123,B234 etc. other than this fromat all needs to be corrected.You just need to response here that your order id  is__.)
Response Instructions:
Identify the user's intent based on their input.
If the user inquires about a book, check the available book data and respond accordingly.
Provide concise, relevant information based on the user's needs along with the human_input.
If user is giving review mention that it is review or order or store policy or book query."""),
          HumanMessagePromptTemplate.from_template("{human_input}"),
      ])

        llm = ChatOpenAI(temperature=0.75,model='gpt-3.5-turbo-1106')    #,model="gpt-4o-mini")
        chat_llm_chain = LLMChain(
              llm=llm,
              prompt=prompt,
              verbose=False,
          )
        response=chat_llm_chain.predict(human_input=query)
        return response

        


    