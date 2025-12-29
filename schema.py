from pydantic import BaseModel, ConfigDict
from typing import List
from typing import Optional

class Article(BaseModel):
    title: str
    content: str
    published: bool
    model_config = ConfigDict(from_attributes=True)

    
    
class UserBase(BaseModel):
    username: str
    email : str
    password : str
 
class UserDisplay(BaseModel):
     username: str
     email: str 
     items: List[Article] = []
     model_config = ConfigDict(from_attributes=True)

          
 # user inside ArticleDisplay
class User(BaseModel):
     id: int
     username: str
     model_config = ConfigDict(from_attributes=True)

              
          
class ArticleBase(BaseModel):
    title: str
    content : str
    published: bool
    creator_id: int
    

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: Optional[User] = None
    model_config = ConfigDict(from_attributes=True)

          
      
    
    