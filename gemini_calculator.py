import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import prompt

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash-002")


def calculate(image):
    response = model.generate_content([prompt, image], stream=True)
    for chunk in response:
        yield chunk.text