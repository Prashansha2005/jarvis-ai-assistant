import os
import google.generativeai as genai

api_key = os.environ.get("GENAI_API_KEY")
if not api_key:
    raise RuntimeError("Set the GENAI_API_KEY environment variable before running this script.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Explain what a black hole is")
print(response.text)
