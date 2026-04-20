from google import genai
import os,io
from dotenv import load_dotenv
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")    
client = genai.Client(api_key=my_api_key)
def debug(images, option):
    prompth = f"Analyze the given code from image and give {option}"
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompth]
    )
    return response.text