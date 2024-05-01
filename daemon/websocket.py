import json
from dacite import from_dict
from websockets.sync.client import connect, ClientConnection
import daemon.methods as methods
import daemon.classes as classes
from rpc.websocket import RPCWS

class DaemonWS(RPCWS):
  def getInfo(self):
    data = self.send(methods.GetInfo)
    return from_dict(data_class=classes.GetInfoResult, data=data)
    
    