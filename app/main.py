from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from typing import List, Optional

import importlib
from os import path, getcwd
import sqlite3

class Profile(BaseModel):
    job: Optional[str] = None
    company: Optional[str] = None
    ssn: Optional[str] = None
    sex: Optional[dict] = None
    name: Optional[List[str]] = []
    birthdate: Optional[str] = None
    username: bool = False

def initialize_database(db_file='/Users/nmaynard/Development/CSI703/finalProject/CSI703-API/data.db'):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def get_profilesz():
    # cursor object
    conn = initialize_database()
    cur = conn.cursor()
  
    # to select all column we will use
    statement = '''SELECT * FROM profiles'''
  
    cur.execute(statement)
  
    print("All the data")
    output = cur.fetchall()
  
    conn.commit()
    # Close the connection
    return output


# Shared propertie


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/profiles")
def get_profiles():
    return get_profilesz()


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}