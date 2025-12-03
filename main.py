from httpx import Headers
from websockets import Response

from Player import Player
from Table import Table

table = Table()

# table.add_player(Player(name="masha"))
# table.add_player(Player(name="dasha"))
#
# table.prepare()
# table.start()
# table.print_winners()

from typing import Union

import uvicorn
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/my_files", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return "Meaw Everyone"

@app.post("/add_player")
def add_player(name: str = Form()):
    table.add_player(Player(name=name))
    return Response(
        status_code=200,
        reason_phrase="OK",
        headers=Headers({"Content-Type": "application/json"})
    )

@app.get("/items/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app)
