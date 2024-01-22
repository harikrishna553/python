import requests
from bs4 import BeautifulSoup

def read_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors

        content = response.text  # The content of the web page as a string

        return content
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def read_url_content_ignore_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text()

        return text_content
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None