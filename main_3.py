from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import time
import asyncio

router = FastAPI()


class TestResponse(BaseModel): 
    elapsed: float 

async def work() -> None: 
    await asyncio.sleep(3) 


@router.get("/")
async def read_root():
    return {"Hello"}


@router.get("/test", response_model=TestResponse) 
async def handler() -> TestResponse: 
    ts1 = time.monotonic() 
    async with asyncio.Lock():
        await work()
    ts2 = time.monotonic() 
    return TestResponse(elapsed=ts2 - ts1) 
