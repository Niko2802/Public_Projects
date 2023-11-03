from fastapi import FastAPI
import asyncio
from uvicorn import run
from pydantic import BaseModel
from time import monotonic

app = FastAPI()

async def work():
  await asyncio.sleep(3)

class TestResponse(BaseModel):
   elapsed: float

@app.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
   ts1 = monotonic()
   await work()
   ts2 = monotonic()
   return TestResponse(elapsed=ts2 - ts1)


if __name__ == "__main__":
   run("main:app", host="127.0.0.1", port=8000, log_level="info")
