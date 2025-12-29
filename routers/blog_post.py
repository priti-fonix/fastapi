'''
Docstring for routers.blog_post

#dictionary unpacking

a = {"x": 1, "y": 2}
b = {"z": 3, **a}
{'z': 3, 'x': 1, 'y': 2}

'''


from urllib import response
from fastapi import APIRouter, Query ,Body,Path
from pydantic import BaseModel,ConfigDict


from enum import Enum
from typing import Optional,List,Dict,Tuple,Set

from fastapi import FastAPI,status,Response

router = APIRouter(
    prefix ='/blog',
    tags=['blog -post'])


class Image(BaseModel):
    url:str
    alias:str
    
class BlogModel(BaseModel):
    title:str
    content:str
    published:Optional[bool]
    tag:List[str] = []
    metadata:Dict[str,str] = {'key1' :'val1'}
    image:Optional[Image] = None
    

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
      
@router.post('/new' #,status_code= status.HTTP_200_OK
             )
def create_blog(blog: BlogModel):
    return{'data':blog}


@router.post('/new/{id}' )
def create_blog(blog: BlogModel,id:int,version:int = 1):
    
    return{
        'data':blog,
        'id':id,
        'data':blog,
        'version':version
        
        }

# ...existing code...

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
    id: int,
    comment_id: int,
    blog: BlogModel,
    comment_title: str = Path(
        ...,
        gt=5,  # gt,ge,lt
        title='Title of the comment',
        description='Description for comment_title',
        alias='comment_Title',
        deprecated=True
    ),
    content: str = Body(
        ...,
        min_length=20,
        regex="^[a-z\\s]+$"  # allowed
    ),
    v: Optional[List[int]] = Query([1, 2, 3, 4, 5])
):
    return {
        "blog": blog,
        "id": id,
        "comment_Title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id
    }


# ...existing code...



# @router.post('/new/{id}/comment')
# def create_comment(blog:BlogModel,id:int,
#                    comment_id:int = Query(None,
#                    title='Id of the  comment',
#                    description='Description for comment_id',
#                    alias='comment_Id',
#                    deprecated=True
#                    ),
#                    # Request----- Body(...) ----
#                    content :str= Body(...,
#                                       min_length=20,
#                                       description=" this is request - body content ",
#                                       regex="^$[a-z/s]"),
#                    v:Optional[List[str]] = Query(None)
#    ):
#     return {
#         'blog':blog,
#         'id':id,
#         'comment_id':comment_id,
#         "content" :content,
#         "version" : v
#     }

# def blog_post_id(id:int,response = Response):
#     blogs =[]
    
#     if(id < 5):
#         response.status_code = status.HTTP_200_OK
#         blogs.insert(id)
#         return {"message" : f" this id {id } is valid"}
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message" : f" this id {id } is invalid"}