from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Project of TV series with FastAPI"
app.version = "0.0.1"

# Generating a class
class Serie(BaseModel):
    id : Optional[int] = None
    title : str
    genre : list
    synopsis : str
    main_cast : list
    year_start : int
    year_end : int


series = [
    {
        "id" : 1,
        "title": "Game of Thrones",
        "genre": ["fantasy", "drama"],
        "synopsis": "Based on George R.R. Martin's novels, it follows the power struggles among noble families as they vie for control of the Iron Throne of the Seven Kingdoms of Westeros.",
        "main cast": ["Emilia Clarke", "Kit Harington", "Peter Dinklage", "Lena Headey"],
        "year start": 2011,
        "year end": 2019
    },
    {
        "id" : 2,
        "title": "Breaking Bad",
        "genre": ["crime", "drama", "thriller"],
        "synopsis": "A high school chemistry teacher turned methamphetamine manufacturer partners with a former student to build a drug empire while dealing with personal and professional challenges.",
        "main cast": ["Bryan Cranston", "Aaron Paul", "Anna Gunn", "Dean Norris"],
        "year start": 2008,
        "year end": 2013
    },
    {
        "id" : 3,
        "title": "Friends",
        "genre": ["comedy", "romance"],
        "synopsis": "Follows the lives, relationships, and comedic antics of six friends living in Manhattan.",
        "main cast": ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"],
        "year start": 1994,
        "year end": 2004
    },
]

# Initial path
@app.get('/', tags = ['Home'])
def message():
    return HTMLResponse('<h1>App working!<h1>')

# Creating new paths
@app.get('/series', tags = ['series'])
def get_series():
    return series

# Path parameters
@app.get('/series/{id}', tags = ['series'])
def get_movie(id : int):
    for serie in series:
        if serie['id'] == id:
            return serie
    return []

# Query parameters
@app.get('/series_one/', tags = ['series'])
def get_serie_by_genre(genre : str):
    for serie in series:
        if genre in serie['genre']:
            return serie
    return ['There is no information']

@app.get('/series_all/', tags = ['series'])
def get_series_by_genre(genre : str):
    series_filtered_genre = [serie for serie in series if genre in serie['genre']]
    return series_filtered_genre
'''
@app.get('/series/', tags = ['series'])
def get_series_by_year_of_start(year_start : int):
    for item in series:
        if str(item['year start']) == str(year_start):
            return item
    return ['There is no information']
'''


# POST method to create new items
'''
# The first form to create new items.
@app.post('/series', tags = ['series'])
def create_serie(id : int = Body(), title : str = Body(), genre : list = Body(), synopsis : str = Body(), main_cast : list = Body(), year_start : int = Body(), year_end : int = Body()):
    series.append({
        "id": id,
        "title": title,
        "genre": genre,
        "synopsis": synopsis,
        "main cast": main_cast,
        "year start": year_start,
        "year end": year_end
    })
    return series'''
# To create new items but avoiding to write every entry to generate new values, we can use the class created before Serie
@app.post('/series', tags = ['series'])
def create_serie(serie : Serie):
    series.append(serie)
    return series

# PUT method to modify information
'''@app.put('/series/{id}', tags=['series'])
def update_movie(id : int , title : str = Body(), genre : list = Body(), synopsis : str = Body(), main_cast : list = Body(), year_start : int = Body(), year_end : int = Body()):
     
     for serie in series:
          if serie['id'] == id:
            serie['title'] = title 
            serie['genre'] = genre 
            serie['synopsis'] = synopsis 
            serie['main cast'] = main_cast
            serie['year start'] = year_start
            serie['year end'] = year_end
            return series
'''
@app.put('/series/{id}', tags=['series'])
def update_movie(id : int , serie : Serie):
     
     for item in series:
          if item['id'] == id:
            item['title'] = serie.title 
            item['genre'] = serie.genre 
            item['synopsis'] = serie.synopsis 
            item['main cast'] = serie.main_cast
            item['year start'] = serie.year_start
            item['year end'] = serie.year_end
            return series


# DELETE method to delete a serie
@app.delete('/series/{id}' , tags = ['series'])

def delete_series(id : int):
    for serie in series:
        if serie['id'] == id:
            series.remove(serie)
            return series