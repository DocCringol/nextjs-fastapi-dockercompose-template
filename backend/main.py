import os
import uvicorn
from fastapi import FastAPI
from fastapi.logger import logger

from routers import api, db_api

HOT_RELOAD = os.getenv("HOT_RELOAD", "0") == "1"
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

app = FastAPI()
app.include_router(api.router)
app.include_router(db_api.router)

@app.get('/')
def root():
	logger.debug("root")
	return "I'm (g)root"

if __name__ == "__main__":
	uvicorn.run(
		"main:app",
		host="0.0.0.0",
		port=5000,
		reload=HOT_RELOAD,
		use_colors=True,
		log_level=LOG_LEVEL,
		access_log=False,
		log_config=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.ini')
	)