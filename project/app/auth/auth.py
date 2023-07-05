from decouple import config

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta

import jwt

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto') #хэширование паролей
    SECRET = config("secret") # .env
    ALGORITHM = config("algorithm") # .env

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)
    
    def verify_password(self, password, hashed_password):
        return self.pwd_context.verify(password, hashed_password)
    

    def encode_token(self, user_id): #jwt  
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=0, seconds=int(config("token_expired_seconds"))),
            'iat': datetime.utcnow(),
            'sub': user_id
        }

        return jwt.encode(
            payload, 
            self.SECRET,
            algorithm = self.ALGORITHM
        )
    
    def decode_token(self, token):
        try: 
            payload = jwt.decode(
                token, 
                self.SECRET,
                algorithms=self.ALGORITHM
            )
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has Expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid Token')
        
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)