import requests
import urllib.parse
import os
import openai

class Wiki:

    def get_wiki_summary(self, page_title):

        openai.api_key = os.getenv("OPENAI_API_KEY")
        encoded_title = urllib.parse.quote(page_title)

        query = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={encoded_title}&formatversion=2&exintro=1&explaintext=1"

        response = requests.get(query)

        response_json = response.json()

        openai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": response_json["query"]["pages"][0]["extract"]
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

        return openai_response["choices"][0]["message"]["content"]