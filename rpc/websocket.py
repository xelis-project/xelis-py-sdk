import json
from websockets.sync.client import connect, ClientConnection
import daemon.methods as methods
import daemon.classes as classes

class RPCWS:
  id: int
  client: ClientConnection
  prefix: str

  def __init__(self, client: ClientConnection) -> None:
    self.id = 0
    self.client = client
    self.prefix = ""
    
  def __createRequestMethod(self, method: str, params = None):
    self.id += 1
    data = { "id": self.id, "jsonrpc": "2.0", "method": method }
    if params is not None:
      data["params"] = params
    
    return json.dumps(data)

  def send(self, method, params = None):
    sendData = self.__createRequestMethod(method=self.prefix+method, params=params)
    self.client.send(sendData)
    
    recvData = self.client.recv()
    data = json.loads(recvData)
    if "error" in data:
      raise ValueError(data["error"]["message"])
    
    return data["result"]
  
  def close(self):
    self.client.close()
  