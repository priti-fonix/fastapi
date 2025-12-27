from fastapi  import FastAPI
from pydantic import BaseModel,field_validator 
from typing import List

app = FastAPI()

#------- pydantic validation ------//
class User(BaseModel):
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str):
        if not value.endswith("@gmail.com"):
            raise ValueError("Only Gmail allowed")
        return value


class  Tea(BaseModel):
    id: int
    name : str
    origin: str
    
teas : list[Tea] = []

@app.get("/")
def read_root():
    return {"message" : "welcome t o the chai charcha "}


@app.get("/teas")
def add_tea():
    # teas.(tea)
    return teas

#---------- apis --------------------------// 
@app.post("/teas")
def add_tea(tea:Tea):
    teas.append(tea)
    return tea

#----------------- path parameters --------------//
@app.put("/teas/{tea_id}")
def update_tea(tea_id:int,updated_tea:Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
        
    return {"error" : "tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id:int):
   for index, tea in enumerate(teas):
        if tea.id == tea_id:
           deleted_tea= tea.pop(index)
           return deleted_tea
        
   return {"error":"tea not found"}       
        
    

    