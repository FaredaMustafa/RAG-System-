#calling a function within fastapi 
from fastapi import FastAPI

app = FastAPI() #create an instance of the FastAPI class

#app is gonna be treated as a decorator to the function welcome() and it will identify the request type of the app, in url path if typed /welcome then the function welcome() will be executed
@app.get("/morning_welcome") #identify request type of the app, in url path if typed /welcome then the function welcome() will be executed
def welcome():
    return {"message": "Welcome to The RAG System"
}
