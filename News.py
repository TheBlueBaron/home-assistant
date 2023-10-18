from dotenv import load_dotenv
import os
import requests

load_dotenv()

class News:

    def get_headlines(self):

        query = f"https://newsapi.org/v2/top-headlines?sources=business-insider-uk&apiKey={os.getenv('NEWSAPI_API_KEY')}"

        response = requests.get(query)

        response_json = response.json()

        headlines = []

        for article in response_json["articles"]:
            headlines.append(article["title"])

        return headlines