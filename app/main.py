from typing import Dict, Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:  # pragma: no cover
    return {"Hello": "World"}


@app.get("/vulnerable/{my_param}")
def vulnerable(my_param: str) -> int:  # pragma: no cover
    import os
    return os.system(my_param)


@app.get("/items/{item_id}")
def read_item(item_id: int,
              q: Union[str, None] = None) -> Dict[str, Union[None, int, str]]:  # pragma: no cover
    return {"item_id": item_id, "q": q}
