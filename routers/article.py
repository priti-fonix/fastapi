from fastapi import APIRouter, Depends
from schema import ArticleDisplay, ArticleBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from typing import List
from auth.oauth2 import oauth2_scheme,get_current_user

from schema import UserBase


router = APIRouter(
    prefix = '/article',
    tags=['article']
    
)

#Create article
@router.post('/',response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


#get specific article
@router.get('/{id}',#response_model = ArticleDisplay
            )
def get_article(id: int, db: Session = Depends(get_db),curent_user: UserBase = Depends(get_current_user)  ):
        return {
            'data': db_article.get_article(db, id),
            'current_user' : curent_user
        }

#  to add authentication to any route [db: Session = Depends(get_db),curent_user: UserBase = Depends(get_current_user) ]-----------------//         
    

#read one user
@router.get('/{id}',response_model= ArticleDisplay)
def get_Single_user(id:int, db: Session = Depends(get_db)):
    return db_article.get_user(db, id)


#update user
@router.put('/{id}',response_model= ArticleDisplay)
def update_user(id:int, request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.update_user(db, id, request)

# delete user
@router.delete('/{id}',response_model= ArticleDisplay)
def update_user(id:int, request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.delete_user(db, id)