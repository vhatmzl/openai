from openai import OpenAI
import os
from PIL import Image
import requests
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL="dall-e-3"

client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
    model=MODEL,
    prompt="아메리칸 숏헤어 고양이랑 폼스키 강아지가 서로 사이 좋게 노는 그림 그려줘",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url

# 저장 파일 이름 설정
filename = 'image.jpg'
response = requests.get(image_url)
with open(filename, 'wb') as f:
    f.write(response.content)
Image.open(filename)