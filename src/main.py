from fastapi import FastAPI
from uvicorn import run

from src.api.crypto import router as crypto


app = FastAPI()
app.include_router(crypto)


if __name__ == "__main__":
    run("main:app", reload=True)
