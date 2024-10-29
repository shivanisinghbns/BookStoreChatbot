from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from Bookstorechatbotwithgpt.main import main_handle  

app = FastAPI()  
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def get_chatbot_interface(request: Request):
    """Serve the chatbot HTML page."""
    return templates.TemplateResponse("chatbot.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(message: Message):
    """Handle user message and return bot response."""
    user_message = message.message
    main_handler = main_handle(user_message) 
    return {"response": main_handler.reponse}
