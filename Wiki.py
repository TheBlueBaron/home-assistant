import requests
import urllib.parse

class Wiki:

    def get_wiki_summary(self, page_title):

        encoded_title = urllib.parse.quote(page_title)

        query = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={encoded_title}&formatversion=2&exsentences=3&exintro=1&explaintext=1"

        response = requests.get(query)

        response_json = response.json()

        return response_json["query"]["pages"][0]["extract"]