import os
import requests
import uvicorn
from fastapi import FastAPI

DEV_MODE = os.getenv("DEV_MODE", "0") == "1"

app = FastAPI()

@app.get("/")
def read_root():
	return True

if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=DEV_MODE)
