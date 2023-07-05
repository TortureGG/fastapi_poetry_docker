from fastapi import FastAPI, HTTPException, Depends
from app.auth.auth import AuthHandler
from app.database import users
from app.schemas import *

print("Api Hello") 
app = FastAPI()
auth_handler = AuthHandler()

# POST  ========================================================
@app.post("/user/register", tags=["user"], status_code=201)
async def register(new_user: UserSchema):
    for user in users:
        if (new_user.auth.email == user['auth']['email']):
            raise HTTPException(status_code=400, detail=f"Email {user['auth']['email']} alredy registered")
    
    hashed_password = auth_handler.get_password_hash(new_user.auth.password)
    new_user.auth.password = hashed_password

    # new_user.auth = new_user.auth.return_json()
    new_user = new_user.return_json()
    #Записываем в БД
    users.append(new_user)

@app.post("/user/login", tags=["user"])
async def login(auth_details: AuthDetails):
    user_login = None
    for user in users: #находим в БД
        if user['auth']['email'] == auth_details.email:
            user_login = user
            break
    
    if (user_login is None): 
        raise HTTPException(status_code=401, detail=f"Invalid email")
    if (not auth_handler.verify_password(auth_details.password, user['auth']['password'])):
        raise HTTPException(status_code=401, detail=f"Invalid password")
    
    token = auth_handler.encode_token(user['auth']['email'])

    # return {'token' : token}
    raise HTTPException(status_code=200, detail={'token' : token})

# TEST ========================================================
@app.get("/protected", tags=["TEST"]) #если токен введен верный
async def protected(email=Depends(auth_handler.auth_wrapper)):
    work = None
    for user in users:
        if(user['auth']['email'] == email):
            work = user['work']
    # return work 
    raise HTTPException(status_code=200, detail={'authenticated': 'Authenticated', 'work' : work})

@app.get("/users", tags=["TEST"])
async def get_users() -> dict:
    return { "data": users}  
