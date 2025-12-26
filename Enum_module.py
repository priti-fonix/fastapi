from enum import Enum

from fastapi import FastAPI,status,Response
from routers import blog_routes,blog_post

#-------------------- predefined parameters ---------------//


app = FastAPI()
app.include_router(blog_routes.router)
app.include_router(blog_post.router)

@app.get("/hello")
def get_welcome():
    return {"message": "Hello world !"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


# #----------------------------- query Parameters ------------------------------//

