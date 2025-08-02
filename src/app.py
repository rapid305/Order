from fastapi import FastAPI
from src._router.api import api_router
from src.database import init_db
# import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)