import os
import uvicorn
from fastapi import FastAPI

from routers import api, db_api

DEV_MODE = os.getenv("DEV_MODE", "0") == "1"

app = FastAPI()
app.include_router(api.router)
app.include_router(db_api.router)

@app.get('/')
def root():
	return "I'm (g)root"

if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=DEV_MODE)
