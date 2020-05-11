from bs4 import BeautifulSoup
import requests
import re
import json


def parse_top_250(name):
    url = 'https://imdb.com/chart/top'
    headers = {'Accept-Language': 'En-us'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    movies = soup.select('td.titleColumn')
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    imdb = []

    for index in range(0, len(movies)):
        cast_string = crew[index]
        cast = cast_string.split()
        director = []
        for i, elem in enumerate(cast):
            if elem == "(dir.),":
                break
            director.append(elem)
        tdir = ' '.join(director) + " (dir.), "
        stars = cast_string.replace(tdir, '')
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index)) + 1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index)) - (len(movie))]
        r = str(round(float(''.join(ratings[index])), 1))
        data = {"Position": place,
                "Year": year,
                "Director": ' '.join(director),
                "Crew": stars,
                "Rating": r}

        data2 = {movie_title: data}
        imdb.append(data2)

    with open(name, 'w') as outfile:
        json.dump(imdb, outfile)
