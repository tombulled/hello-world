from fastapi import FastAPI
from typing import Mapping

app: FastAPI = FastAPI()


@app.get("/")
def get_root() -> Mapping[str, str]:
    return {"message": "Hello, World!"}
