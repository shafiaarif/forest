import requests
import json

# Base URL for the FastAPI backend
BASE_URL = "http://localhost:8000"

def insert_data(      
        slug: str,
        title_en: str,
        title_ur: str,
        content_en: str,
        content_ur: str
        ):
    url = f"{BASE_URL}/chatbots"
    payload = {
        "slug":slug,
        "title_en":title_en ,
        "title_ur":title_ur,
        "content_en": content_en,
        "content_ur": content_ur   
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("data inserted successfully")
        print(json.dumps(response.json(), indent=2))
    else:
        print("failed to insert:", response.text)

insert_data(slug= "urban-forest-intro",
  title_en="Introduction to Urban Forests",
  title_ur= "شہری جنگلات کا تعارف",
  content_en="Urban forests play a critical role in improving air quality, reducing heat, and enhancing biodiversity in cities.",
  content_ur= "شہری جنگلات ہوا کے معیار کو بہتر بنانے، گرمی کو کم کرنے، اور شہروں میں حیاتیاتی تنوع کو بڑھانے میں اہم کردار ادا کرتے ہیں")