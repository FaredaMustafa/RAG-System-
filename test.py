from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
async def get():
    return {"message": "welcome to the RAG system"}

@app.post(path="/")
async def post():
    return {"message": "this is a post request"}

@app.put(path="/{id}")
async def put(id: int):
    return {"message": f"this is a put request for id {id}"}


# @app.post("/", deprecated=True) #"deprecated"  means this endpoint should not be used anymore
# async def post():
#     return {"message": "this is a post request"}


#static parameter shold be before the dynamic parameter otherwise it will be treated as a dynamic parameter and the static parameter will never be reached
@app.get("/Admin/1", include_in_schema=False) #include_in_schema=False means this endpoint will not be included in the documentation
async def get_admin_id():
    return {"message": f"this is a get request for admin users :"}

@app.get(f"/admin/2/{{admin_id}}")
async def get_admin(admin_id: str):
    return {"message": f"this is a get request for admin users with id : {admin_id}"}

#dynamic parameter
@app.get("/Users/{user_id}")
async def get_user_id(user_id: str):
    return {"message": f"this is a get request for user id : {user_id}"}

@app.get("/manager/{user_id}")
async def get_manager(user_id: str):
    return {"message": f"this is a get request for manager id : {user_id}"}


class UsersList(str, Enum):
    admin = "admin"
    manager = "manager"
    user = "user"

@app.get("/user_type(user_type: UsersList, user_id: str)")
async def get_user_type(user_type: UsersList, user_id: str):
    return {"message": f"this is a get request for user type : {user_type} with id : {user_id}"}