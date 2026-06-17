from fastapi import FastAPI # Import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Imports CORS middleware 
# FastAPI:  like engine for websites
# CORS middleware:  like agent who says: browser! he's working with FastAPI

app = FastAPI()  # create FastAPI

app.add_middleware( 
    CORSMiddleware,  # The one that allows cross-origin requests
    allow_origins=["http://localhost:5173"],  # Allow requests ONLY from React server
    allow_methods=["*"],  # Allow any HTTP methods: GET, POST, PUT, DELETE, etc.
    allow_headers=["*"]   # Allow any headers
)

@app.get("/")
def root():
    return{"message: KalKro Backend works."}