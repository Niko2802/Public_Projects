
from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel
import time
import asyncio

router = FastAPI()

work_lock = asyncio.Lock()

class TestResponse(BaseModel): 
    elapsed: float 

async def work() -> None: 
    await asyncio.sleep(3) 

task = asyncio.create_task(work())

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/test", response_model=TestResponse) 
async def handler() -> TestResponse: 
    ts1 = time.monotonic() 
    print(ts1)
    await task
    print("end lock")
    # ... организация вызовы функции work() ... 
    ts2 = time.monotonic() 
    print(ts2)
    return TestResponse(elapsed=ts2 - ts1) 
