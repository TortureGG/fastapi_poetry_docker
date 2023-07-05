from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime, timedelta
from typing import Optional

class Position(Enum):
    intern = "intern"
    worker = "worker"
    expert = "expert"
    cleaner = "cleaner"

class PositionSchema(BaseModel): #Схема должность работника
    position: Position
    sellary: float = Field(ge=0)
    hired_at: Optional[datetime] = datetime.utcnow()
    promotion_at: Optional[datetime] = datetime.utcnow() + timedelta(days=30)

    def return_json(self):
        json = {
            'position': self.position,
            'passellarysword': self.sellary, 
            'hired_at': self.hired_at, 
            'promotion_at': self.promotion_at
        }
        return json

class AuthDetails(BaseModel): #Схема для авторизации
    email: EmailStr = Field(...)
    password: str = Field(...)

    def return_json(self):
        json = {
            'email': self.email,
            'password': self.password
        }
        return json

    class Config:
        schema_extra = {
            "example": {
                "email": "Roma@mail.com",
                "password": "1234"
            }
        }

class UserSchema(BaseModel): #Схема профиля пользователя
    id: Optional[int] = Field(ge=0) 
    fullname: Optional[str] = "None"
    work: Optional[list[PositionSchema]] = []
    auth: AuthDetails #email password

    def return_json(self):
        work = []
        for w in self.work:
            work.append(w.return_json())
            
        json = {
            'id': self.id,
            'fullname': self.fullname,
            'work': work,
            'auth': self.auth.return_json()
        }
        return json

    class Config:
        schema_extra = {
            "example": {
                "id": 0,
                "fullname": "Maxim",
                "work":[{'position':Position.intern, 
                         'sellary':5005, 
                         'hired_at': datetime.utcnow(), 
                         'promotion_at': datetime.utcnow() + timedelta(days=30)}],
                
                # "work":[{'position':'expert', 'sellary':5005}],
                "auth":{
                        "email": "Maxim@mail.com",
                        "password": "weakpassword"
                    }
            }
        }