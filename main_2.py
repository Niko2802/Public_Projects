from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import time
import asyncio

router = FastAPI()


class TestResponse(BaseModel): 
    elapsed: float 

def work() -> None: 
    print ("start work")
    time.sleep(5)
    print ("end work")


@router.get("/")
def read_root():
    return {"Hello"}


@router.get("/test", response_model=TestResponse) 
def handler() -> TestResponse: 
    print("start handler")
    ts1 = time.monotonic() 
    work()
    ts2 = time.monotonic() 
    print("end handler")
    return TestResponse(elapsed=ts2 - ts1) 
