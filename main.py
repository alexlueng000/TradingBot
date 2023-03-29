
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient

from api.stocks import router as stock_router


# define origins
origins = ["*"]

# initialize FastAPI
app = FastAPI()

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_event():
    app.mongodb_client = AsyncIOMotorClient("mongodb://localhost:27017")
    app.mongodb = app.mongodb_client["gpt-trading"]

@app.on_event("shutdown")
async def shutdown_db_event():
    app.mongodb_client.close()

app.include_router(stock_router, prefix="/stocks", tags=["stocks"])


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
