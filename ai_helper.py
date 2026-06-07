import warnings
warnings.filterwarnings("ignore")

import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-flash-lite-latest")


def ask_ai(question):
    try:
        prompt = f"""
        You are Trivya AI, a voice assistant.
        Answer the user's question in under 50 words.
        Keep responses concise and easy to speak aloud.

        Question: {question}
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"AI Error: {e}"