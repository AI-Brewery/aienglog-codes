import os
from dotenv import load_dotenv
from google import genai


load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("GEMINI_API_KEY")
# Initialize the client (assumes GEMINI_API_KEY is set)
client = genai.Client(api_key=api_key)


# Send a request
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words"
)

# Print the response
print(response.text)


# from google import genai
# from google.genai import types

# # Initialize the client
# client = genai.Client(api_key=api_key)

# # Send a request with thinking disabled
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain how AI works in a few words",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_budget=0)  # Disables thinking
#     ),
# )

# # Print the response
# print(response.text)
