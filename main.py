from typing import Union
from fastapi import FastAPI
from  pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None] = None

@app.get('/')
def read_root():
    return{'Hello': 'World'}

@app.get('/hola')
def hola_mundo():
    return{'hola':'Mundo'}

@app.get('/items/{item_id}')
def read_item(item_id: int,q:Union[str,None] = None):
    return {'item_id':item_id, 'q': q}

@app.get('/calculadora')
def calculadora(operado_1: float, operado_2:float):
    return {'suma': operado_1 + operado_2}