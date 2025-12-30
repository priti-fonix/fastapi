from fastapi import APIRouter,HTTPException,status, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from db.hash import Hash
from auth import oauth2
from dotenv import load_dotenv
import os
load_dotenv()


router = APIRouter(
    tags=['authentication']
)
@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Dbuser).filter(models.Dbuser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify( request.password ,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    access_token = oauth2.create_access_token(data={'sub': user.username})
    
    return {
        'access_token': access_token,
        "token_type": 'bearer',
        'user_id': user.id,
        'username': user.username
    }
    
    '''
    {
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyaWRoaSIsImV4cCI6MTc2NzA3NTgzMn0.TJItb2Crroqc4Nge_SiEm3ZkxTvyjlyum5denTbIhhg",
  "token_type": "bearer",
  "user_id": 10,
  "username": "ridhi"
}
    
    
    '''