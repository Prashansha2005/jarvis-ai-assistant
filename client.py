import google.generativeai as genai

# Replace with your actual API key from https://makersuite.google.com/app/apikey
genai.configure(api_key="AIzaSyClmugZy06i0WS4PIpzw_P2NzIupFu53_s")

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # or "gemini-pro"

# Generate content
response = model.generate_content("do you love me")

# Print the response
print(response.text)
