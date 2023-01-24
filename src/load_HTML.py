import requests
from ..config import headers, afisha_url, encoding

def store_url_page_locally(url):

    response = requests.get(url, headers = headers)

    htmlPage = response.text

    with open ('data/index.html', 'w', encoding = encoding) as file:
        file.write(htmlPage)

store_url_page_locally(afisha_url)