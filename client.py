import google.generativeai as genai

genai.configure(api_key="AIzaSyClmugZy06i0WS4PIpzw_P2NzIupFu53_s")
model = genai.GenerativeModel(model_name="gemini-1.5-flash") 
response = model.generate_content("do you love me")
print(response.text)
