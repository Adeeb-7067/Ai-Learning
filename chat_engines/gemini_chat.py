import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# chat_engines/gemini_chat.py
def chat_with_gemini_streaming(prompt):
    try:
        response = model.generate_content(prompt, stream=True)

        streamed_text = ""
        for chunk in response:
            if chunk.text:
                print(chunk.text, end='', flush=True)
                streamed_text += chunk.text
        print()  # Newline after response finishes
        return streamed_text.strip()

    except Exception as e:
        print(f"⚠️ Error during Gemini streaming: {e}")
        return None

