Сделать сервис на FastAPI, предоставляющий один метод: 
  GET /test 

  В качестве полезной работы метод спит 3 секунды: 

  async def work() -> None: 
      asyncio.sleep(3) 

  При этом не допускается одновременная работа нескольких функций work() 

  В качестве ответа метод возвращает фактически затраченое время на обработку запроса: 

  class TestResponse(BaseModel): 
      elapsed: float 

  @router.get("/test", response_model=TestResponse) 
  async def handler() -> TestResponse: 
      ts1 = monotonic() 
      ... организация вызовы функции work() ... 
      ts2 = monotonic() 
      return TestResponse(elapsed=ts2 - ts1) 

  Тестирование: 
  Метод считается успешным, если при одновременном вызове каждый возвращающийся 
  ответ содержит elapsed отличающийся от предыдущего не менее чем на 3 секунды