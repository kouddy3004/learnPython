from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from learnAny.learnfastApi.backEnd.models import MovieDb

origins = [
    "http://localhost:3000",  # Default Vite/React/Preact port
    "http://127.0.0.1:3000",
]

run = FastAPI()

run.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@run.get("/")
def home():
    welcomeMsg="This Api is Created by Koushik for searching Movies downloaded from Kaggle"
    return welcomeMsg

@run.get("/movies")
def movies():
    obj=MovieDb()
    #To convert dataframe to html table
    html_table = obj.getAllMovies().to_html(index=False)
    return HTMLResponse(content=html_table, status_code=200)

@run.get("/movies/{name}")
def movies(name: str):    
    obj=MovieDb()
    #To convert dataframe to html table
    html_table = obj.getAllMovies(name).to_html(index=False)
    return HTMLResponse(content=html_table, status_code=200)


