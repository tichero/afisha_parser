import random
from time import sleep
import json
from src.config import encoding
from src.parse_genre import parse_genre

with open("data/all_genres_dict.json", 'r', encoding=encoding) as file:
    all_genres = json.load(file)

iteration_count = int(len(all_genres) - 1)
print(f'Всего итераций: {iteration_count}')

for count, (genre_name, genre_href) in enumerate(all_genres.items()):

    parse_genre(genre_name, genre_href, count)

    print(f'Итерация {count}. {genre_name} записан')
    iteration_count = iteration_count - 1
    if iteration_count == 0:
        print('Работа окончена')
        break

    print(f'Осталось итераций: {iteration_count}')
    sleep(random.randrange(2, 4))

