from fastapi import FastAPI

import asyncio

import uvicorn

from app.database.run import create_database


app = FastAPI(title="Diary")

async def init_app():
    await create_database()
    
    
@app.get('/')
async def hello() -> str:
    return "Hello"


if __name__ == "__main__":
    
    asyncio.run(init_app())
    
    uvicorn.run(app=app, host="127.0.0.1", port=8000, reload=True)