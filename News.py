import os
import requests
from bs4 import BeautifulSoup
import openai

class News:

    def query_news_source(self, news_source):

        query = f"https://newsapi.org/v2/top-headlines?sources={news_source}&apiKey={os.getenv('NEWSAPI_API_KEY')}"

        response = requests.get(query)

        response_json = response.json()

        return response_json        

    def get_headlines(self):

        news_source_query = self.query_news_source("bbc-news")

        headlines = []

        for article in news_source_query["articles"]:
            headlines.append(article["title"])

        return headlines

    def get_top_story(self):

        openai.api_key = os.getenv("OPENAI_API_KEY")

        news_source_query = self.query_news_source("bbc-news")

        urls = []
        stripped_paragraphs = []

        for article in news_source_query["articles"]:
            urls.append(article["url"])

        news_html_text = requests.get(urls[0]).text
        soup = BeautifulSoup(news_html_text, 'html.parser')
        paragraphs = soup.find_all('p')

        for p in paragraphs:
            stripped_paragraphs.append(p.get_text())

        openai_content = " ".join(stripped_paragraphs)

        openai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": openai_content
                },
                {
                    "role": "system",
                    "content": "You are a serious assistant.\n\nWrite a summary of the following text in no more than 5 sentences."
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        print(openai_response["choices"][0]["message"]["content"])
        return openai_response["choices"][0]["message"]["content"]