from fastapi import FastAPI, Body, Path , Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from jwt_manager import create_token

app = FastAPI()
app.title = "Project of TV series with FastAPI"
app.version = "0.0.1"

# Creating a new class which allows us to save user information
class  User(BaseModel):
    email : str
    password : str

# Generating a class
class Serie(BaseModel):
    id : Optional[int] = None
    title : str = Field(min_length= 5 , max_length = 20) #This line restricts input to minimum 5 digits and at most 20 digits only
    genre : list
    synopsis : str
    main_cast : list
    year_start : int = Field(le = 2024)
    year_end : int = Field(le = 2024)
    #year_end : int = Field(default = 2000, le = 2024)

    #To define default values we use
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id" : 1,
                    "title" : "This is a serie",
                    "genre" : ["Uknown"],
                    "synopsis": "Without a synopsis",
                    "main_cast" : ["Uknown"],
                    "year_start" : 1990,
                    "year_end" : 2000
                }
            ]
        }
    }
    

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

# Create a new route to capture data of the user
@app.post('/login', tags = ['auth'])
def login(user : User):
    return user


# Creating new paths
@app.get('/series', tags = ['series'], response_model = List[Serie] , status_code = 200)
def get_series() -> List[Serie]:
    return JSONResponse(status_code = 200 , content = series)

# Path parameters
@app.get('/series/{id}', tags = ['series'] , response_model = Serie)
def get_serie(id : int = Path(ge = 1, le = 2000)) -> Serie:
    for serie in series:
        if serie['id'] == id:
            return JSONResponse(content = serie)
    return JSONResponse(status_code = 404 , content = [])

# Query parameters
@app.get('/series_one/', tags = ['series'] , response_model = Serie)
def get_serie_by_genre(genre : str = Query(min_length = 4 , max_length = 20)) -> Serie:
    for serie in series:
        if genre in serie['genre']:
            return JSONResponse(content = serie)
    return JSONResponse(content = [])

@app.get('/series_all/', tags = ['series'] ,response_model = List[Serie])
def get_series_by_genre(genre : str) -> List[Serie]:
    series_filtered_genre = [serie for serie in series if genre in serie['genre']]
    return JSONResponse(content = series_filtered_genre)
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
@app.post('/series', tags = ['series'], response_model = dict , status_code = 201)
def create_serie(serie : Serie) -> dict:
    series.append(serie)
    #return series
    return JSONResponse(status_code = 201 , content = {"message" : "The movie has been recorded."})

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
@app.put('/series/{id}', tags=['series'] , response_model = dict , status_code = 200)
def update_movie(id : int , serie : Serie) -> dict:
     
     for item in series:
          if item['id'] == id:
            item['title'] = serie.title 
            item['genre'] = serie.genre 
            item['synopsis'] = serie.synopsis 
            item['main cast'] = serie.main_cast
            item['year start'] = serie.year_start
            item['year end'] = serie.year_end
            #return series
            return JSONResponse(status_code = 200 , content = {"message" : "TThe movie has been modified."})


# DELETE method to delete a serie
@app.delete('/series/{id}' , tags = ['series'], response_model = dict, status_code = 200)

def delete_series(id : int) -> dict:
    for serie in series:
        if serie['id'] == id:
            series.remove(serie)
            #return series
            return JSONResponse(status_code = 200 , content = {"message" : "TThe movie has been deleted."})