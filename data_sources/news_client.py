import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(query: str, limit: int = 5):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "pageSize": limit,
        "apiKey": NEWS_API_KEY,
        "language": "en"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("News API failed")

    articles = response.json()["articles"]

    return [{"title": a["title"]} for a in articles]


