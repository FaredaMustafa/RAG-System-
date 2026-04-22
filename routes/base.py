#all routes related to the base of the application will be defined in this file
from fastapi import FastAPI, APIRouter
import os
from dotenv import load_dotenv

load_dotenv(".env") # load environment variables from the .env file
base_router = APIRouter(
    prefix="/base",
    tags= ["Base_route_api"]
)

@base_router.get("/")
def welcome():
    app_name = os.environ.get("APP_NAME")
    app_version = os.environ.get("APP_VERSION")
    return {"message": f"Welcome to {app_name} version {app_version}"} 