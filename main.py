from enum import Enum

from fastapi import FastAPI,status,Response, Request
from routers import blog_get
from routers import blog_post
from routers import user,article
from routers import product,file

from auth import authentication
from db import models
from db.database import engine
from exceptions import storyException
from fastapi.responses import JSONResponse,PlainTextResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
#-------------------- predefined parameters ---------------//



app = FastAPI()

# Serve static files from the 'files' directory at '/files'
app.mount("/files", StaticFiles(directory="files"), name="files")

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(file.router)

@app.get("/hello")
def get_welcome():
    return {"message": "Hello world !"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#-------------------- error handler ------------------- //
@app.exception_handler(storyException)
def story_exception_handler(request : Request, exc: storyException
):
    return JSONResponse(
        status_code=418,
        content = {'detail': exc.name}
    )

#----------- custom exception handler -----------------//
@app.exception_handler(HTTPException)
def custom_handler(request : Request, exc: storyException
):
    return PlainTextResponse(str(exc),status_code=400)
     
# -----------------  creating table in db -------------//

models.Base.metadata.create_all(engine)

#---- CORS - SETUP ------//
origins = [
    'http://localhost:3000'
    
]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.mount("/files", StaticFiles(directory="files"), name="files")
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


# #----------------------------- query Parameters ------------------------------//

