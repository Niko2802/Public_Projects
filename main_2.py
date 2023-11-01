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

PARALLEL = 1
INTERVAL = 3

semaphore = asyncio.Semaphore(PARALLEL)

# async def work():
#     async with semaphore:
#             start = time.time()
#             try:
#                 asyncio.sleep(3)
#             finally:
#                 ellapsed = time.time() - start
#                 # wait to liberate semaphore:
#                 await asyncio.sleep(INTERVAL - ellapsed) 


@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/test", response_model=TestResponse) 
async def handler() -> TestResponse: 
    ts1 = time.monotonic() 
    print(ts1)
    # async with semaphore:
    print("start semaphore")
    await asyncio.wait_for(work(), timeout=10)
    print("end semaphore")
    # ... организация вызовы функции work() ... 
    ts2 = time.monotonic() 
    return TestResponse(elapsed=ts2 - ts1) 
