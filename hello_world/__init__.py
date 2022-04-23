from fastapi import FastAPI
from typing import Dict

app: FastAPI = FastAPI()


@app.get("/")
def get_root() -> Dict[str, str]:
    return {"message": "Hello, World!"}
