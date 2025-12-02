# from Player import Player
# from Table import Table
#
# table = Table()
# table.add_player(Player(name="misha"))
# table.add_player(Player(name="masha"))
# table.add_player(Player(name="dasha"))
#
# table.prepare()
# table.start()
# table.print_winners()

from typing import Union

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/my_files", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return "Meaw Everyone"


@app.get("/items/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app)
