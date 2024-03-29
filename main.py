from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Project of TV series with FastAPI"
app.version = "0.0.1"

series = [
    {
        "Title": "Game of Thrones",
        "Genre": ["Fantasy", "Drama"],
        "Synopsis": "Based on George R.R. Martin's novels, it follows the power struggles among noble families as they vie for control of the Iron Throne of the Seven Kingdoms of Westeros.",
        "Main Cast": ["Emilia Clarke", "Kit Harington", "Peter Dinklage", "Lena Headey"]
    },
    {
        "Title": "Breaking Bad",
        "Genre": ["Crime", "Drama", "Thriller"],
        "Synopsis": "A high school chemistry teacher turned methamphetamine manufacturer partners with a former student to build a drug empire while dealing with personal and professional challenges.",
        "Main Cast": ["Bryan Cranston", "Aaron Paul", "Anna Gunn", "Dean Norris"]
    },
    {
        "Title": "Friends",
        "Genre": ["Comedy", "Romance"],
        "Synopsis": "Follows the lives, relationships, and comedic antics of six friends living in Manhattan.",
        "Main Cast": ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
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