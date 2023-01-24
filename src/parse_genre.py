import requests
import json
import csv
from bs4 import BeautifulSoup
from src.config import encoding


def parse_genre(genre_name, genre_ref, count = ""):
    try:
        with open(f"data/{count}_{genre_name}.html", 'r', encoding=encoding) as file:
            htmlPage = file.read()
    except:
        htmlPage = requests.get(genre_ref).text
        
        with open(f"data/{count}_{genre_name}.html", 'w', encoding=encoding) as file:
            file.write(htmlPage)
    
    soup = BeautifulSoup(htmlPage,"lxml")

    film_data = soup.find_all(class_="movieList_item")
    
    
    film_info = []
    for item in film_data:
        film_param = item.find(class_="movieItem_info")

        title = film_param.find("a").text
        genres = film_param.find(class_="movieItem_genres").text
        year = film_param.find(class_="movieItem_year").text
        rate = film_param.find(class_="rating_num").text

        film_info.append(
            {
                "Title":title,
                "Genres":genres,
                "Year":year,
                "Rate":rate
            }
        )

        with open(f"data/{count}_{genre_name}.csv", "a", encoding=encoding) as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    genres,
                    year,
                    rate
                )
            )

        with open(f"data/{count}_{genre_name}.json", "a", encoding=encoding) as file:
            json.dump(film_info, file, indent=4, ensure_ascii=False) 

parse_genre("анимация", "https://www.kinoafisha.info/rating/movies/animation/")