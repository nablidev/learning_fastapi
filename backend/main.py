#main.py
import uvicorn
from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    return {"msg": "Hello API"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
