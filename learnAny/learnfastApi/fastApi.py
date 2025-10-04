from fastapi import FastAPI
from fastapi.responses import HTMLResponse

run = FastAPI()

@run.get("/")
def home():
    welcomeMsg="This Api is Created by Koushik for searching Movies downloaded from Kaggle"
    return welcomeMsg

@run.get("/movies")
def movies():
    from learnAny.learnfastApi.models import MovieDb
    obj=MovieDb()
    #To convert dataframe to html table
    html_table = obj.getAllMovies().to_html(index=False)
    return HTMLResponse(content=html_table, status_code=200)

@run.get("/movies/{name}")
def movies(name: str):
    from learnAny.learnfastApi.models import MovieDb
    obj=MovieDb()
    #To convert dataframe to html table
    html_table = obj.getAllMovies(name).to_html(index=False)
    return HTMLResponse(content=html_table, status_code=200)

