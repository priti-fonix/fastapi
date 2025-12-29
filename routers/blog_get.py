from fastapi import APIRouter

from enum import Enum
from typing import Optional

from fastapi import FastAPI,status,Response

router = APIRouter(prefix ='/blog')

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

@router.get('/all',tags =['blog'],
         summary = "To fetch all blogs",
         description = "this fetches all  the records  in the blog",
         response_description="this is the all blog list")
def get_all_blog(page=1,page_size=10):
    return {"message":f"this is {page} and size of page - size is {page_size} "}


@router.get('/{id}',tags =['blog'])
def get_all_blog(id:int):
    return {"message":f"this is blog with id {id}  "}

@router.get('/all/optional',tags =['blog'])
def get_all_blog(page=1,page_size: Optional[int]=None):
    return {"message":f"this is {page} and size of page  is {page_size} "}


@router.get('/{id}/comments/{comment_id}',tags =['blog','comment'])
def get_all_blog(id: int, comment_id:int,valid:bool = True,username: Optional[str] = None):
    return {"message":f"this is {comment_id} by  { username} at this blog id: {id} "}

@router.get('/{id}',status_code= status.HTTP_200_OK,tags =['blog'])
def get_Blog(id:int,response = Response):
    if id < 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':"blog with id {id} is not here"}
    else:
        response.status_code = status.HTTP_200_OK  
        return {"message":"blog with {id } is  found"}
    
    