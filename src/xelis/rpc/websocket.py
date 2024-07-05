import asyncio
import json
from typing import Any
from websockets.client import WebSocketClientProtocol

class RPCWS:
  id: int
  client: WebSocketClientProtocol
  prefix: str
  _listenTask: asyncio.Task
  _queues: dict[int, asyncio.Queue]
  _events: dict[str, int]

  def __init__(self, client: WebSocketClientProtocol) -> None:
    self.id = 0
    self.client = client
    self.prefix = ""
    self._queues = {}
    self._events = {}
    self._listenTask = asyncio.create_task(self.__listen())
    
  async def __listen(self):
    while True:
      dataRecv = await self.client.recv()
      data = json.loads(dataRecv)
      id = data["id"]
      if id in self._queues:
        await self._queues[id].put(data)
      
  def __createRequestMethod(self, method: str, params: dict[Any, Any] = None):
    self.id += 1
    data = { "id": self.id, "jsonrpc": "2.0", "method": method }
    if params is not None:
      data["params"] = params
    
    return json.dumps(data), self.id

  async def send(self, method: str, params = None):
    sendData, id = self.__createRequestMethod(method=self.prefix+method, params=params)
    await self.client.send(sendData)
    
    recvQueue = asyncio.Queue()
    self._queues[id] = recvQueue
    
    data = await recvQueue.get()
    del self._queues[id]
  
    if "error" in data:
      err = data["error"]["message"]
      raise ValueError(err)
    else:
      result = data["result"]
      return result
       
  async def listenEvent(self, event: str):
    recvQueue = None
    firstResponse = None
    id = None
    
    if event not in self._events:
      sendData, id = self.__createRequestMethod(method="subscribe", params={ "notify": event })
      await self.client.send(sendData)
    
      self._events[event] = id
      recvQueue = asyncio.Queue()
      self._queues[id] = recvQueue
      firstResponse = True
    else:
      firstResponse = False
      id = self._events[event]
      recvQueue = self._queues[id]

    while True:
      data = await recvQueue.get()
      
      if data is None:
        del self._queues[id]
        del self._events[event]
        return
      
      if "error" in data:
        err = data["error"]["message"]
        raise ValueError(err)
      else:
        if not firstResponse:
          result = data["result"]
          return result

        firstResponse = False
      
  async def closeEvent(self, event: str):
    if event in self._events:
      id = self._events[event]
      await self.send("unsubscribe", { "notify": event })
      await self._queues[id].put(None)

  async def close(self):
    await self.client.close()
    return self._listenTask.cancel()
  