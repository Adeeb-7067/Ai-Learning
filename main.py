# "SIMPLE CHATBOT USING GEMINI"  
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load API key
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     print("❌ GEMINI_API_KEY not found in .env file")
#     exit(1)

# # Configure Gemini
# genai.configure(api_key=api_key)

# # Use a working model you have access to
# model = genai.GenerativeModel("gemini-1.5-pro-latest")
# chat = model.start_chat(history=[])

# def chat_with_ai(prompt):
#     try:
#         response = chat.send_message(prompt)
#         return response.text
#     except Exception as e:
#         print("⚠️ Error during Gemini API call:", e)
#         return None

# # Chat loop
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         break
#     response = chat_with_ai(user_input)
#     if response:
#         print("AI:", response)
#     else:
#         print("⚠️ Failed to get a response from Gemini.")


from profiles_loader import get_profile_by_name
from context_builder import format_profile
from chat_engines.gemini_chat import chat_with_gemini_streaming

print("\U0001F916 ChatBot with Profile Context (Gemini)")
print("Type 'exit' to quit.\n")

chat_history = []
while True:
    name_input = input("🔍 Enter full name (e.g. John Doe): ").strip()
    if name_input.lower() in ["exit", "quit"]:
        break

    profile = get_profile_by_name(name_input)
    if not profile:
        print("❌ Profile not found.\n")
        continue

    question = input("❓ What do you want to ask about this profile? ")
    context = format_profile(profile)
    full_prompt = f"{context}\n\nAnswer this question about the profile: {question}"

    answer = chat_with_gemini_streaming(full_prompt)
    if answer:
        print(f"\n🤖 Gemini: {answer}\n")        
    else:
        print("⚠️ Failed to get a response from Gemini.\n")

    while True:
        question = input("❓ Ask about this profile (or type 'back' to change profile): ")
        if question.lower() in ["back", "exit", "quit"]:
            break

        chat_history.append(f"User: {question}")
        full_prompt = "\n".join(chat_history)
        answer = chat_with_gemini_streaming(full_prompt)
        if answer:
            print(f"\n🤖 Gemini: {answer}\n")
            chat_history.append(f"Assistant: {answer}")
        else:
            print("⚠️ No response.\n")
