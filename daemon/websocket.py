import json
from dacite import from_dict
from websockets.sync.client import connect, ClientConnection
import daemon.methods as methods
import daemon.classes as classes
from rpc.websocket import RPCWS

class DaemonWS(RPCWS):
  def __init__(self, client: ClientConnection = None, url: str = None) -> None:
    if url is not None:
      client = connect(uri=url)

    super().__init__(client)
  
  def getInfo(self):
    data = self.send(methods.GetInfo)
    return from_dict(data_class=classes.GetInfoResult, data=data)
    
    