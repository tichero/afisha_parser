from bs4 import BeautifulSoup
from bs4.element import Tag
from config import encoding
import json

def parse_genres_to_json():
    with open("data/index.html", "r", encoding = encoding) as file:
        htmlPage = file.read()

    soup = BeautifulSoup(htmlPage, "lxml")

    genres_table_root = soup.find(class_="ratings coating-adaptive-main")
    genres_table = genres_table_root.find(class_="column-width grid")

    genres_links = {}

    child:Tag
    for child in genres_table.find_all():
        genres_links[child.text] = child["href"]

    with open ('data/all_genres_dict.json', 'w', encoding = encoding) as file: 
        json.dump(genres_links, file, indent=4, ensure_ascii=False)

parse_genres_to_json()
