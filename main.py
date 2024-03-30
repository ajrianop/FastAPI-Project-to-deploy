from fastapi import FastAPI
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
        "main Cast": ["Emilia Clarke", "Kit Harington", "Peter Dinklage", "Lena Headey"],
        "year start": 2011,
        "year finalization": 2019
    },
    {
        "id" : 2,
        "title": "Breaking Bad",
        "genre": ["crime", "drama", "thriller"],
        "synopsis": "A high school chemistry teacher turned methamphetamine manufacturer partners with a former student to build a drug empire while dealing with personal and professional challenges.",
        "main Cast": ["Bryan Cranston", "Aaron Paul", "Anna Gunn", "Dean Norris"],
        "year start": 2008,
        "year finalization": 2013
    },
    {
        "id" : 3,
        "title": "Friends",
        "genre": ["comedy", "romance"],
        "Synopsis": "Follows the lives, relationships, and comedic antics of six friends living in Manhattan.",
        "main Cast": ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"],
        "year start": 1994,
        "year finalization": 2004
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

@app.get('/series/{id}', tags = ['series'])
def get_movie(id : int):
    for serie in series:
        if serie["id"] == id:
            return serie
    return []

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
