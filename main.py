from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Project of TV series with FastAPI"
app.version = "0.0.1"

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


# POST method
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
    return series
