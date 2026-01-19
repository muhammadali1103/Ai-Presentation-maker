import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your API key for Google Gemini
api_key = "AIzaSyDkA34qE5jScjasD02k3KTqQrr2wicYxTw"
genai.configure(api_key=api_key)

def chat_development(user_message):
    conversation = build_conversation(user_message)
    try:
        assistant_message = generate_assistant_message(conversation)
    except Exception as e:
        assistant_message = "Error occurred: " + str(e)

    return assistant_message

def build_conversation(user_message):
    return [
        {"text": "You are an assistant that gives ideas for PowerPoint presentations. "
                 "When answering, provide the summarized content for each slide based on the number of the slide. "
                 "The format of the answer must be: Slide X: {title of the content} \n Content: \n {bullet points} "
                 "Keyword: \n {most important keyword for the slide, 2 words max}"},
        {"text": user_message}
    ]

def generate_assistant_message(conversation):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Select the model (adjust as needed)
    
    # Generate content based on the conversation
    response = model.generate_content(conversation)
    
    # Return the response content
    return response.text
