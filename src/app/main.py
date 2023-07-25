from fastapi import FastAPI
from mangum import Mangum
from .logic.move_logic import choose_direction

app = FastAPI()

# TODO: Implement my logic here to handle the requests from Battlesnake

@app.get("/")
def read_root(): 
    return {
            "apiversion": "1",
            "author": "VictorGasperi",
            "color": "#FF1493",
            "head": "evil",
            "tail": "bolt",
            "version": "0.0.1-beta"
            }

@app.post("/move")
def move(request: dict):
    direction = choose_direction(request)
    return {
    "move": direction,
    "shout": "What will be my next move ?"
}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/create_item")
def create_item(request: dict):
    item_id = request.get("item_id")
    name = request.get("name")

    return {"item_id": item_id,
            "name": name}   


handler = Mangum(app, lifespan="off")
