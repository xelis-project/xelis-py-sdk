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
    data = self.send(method=methods.GetInfo)
    return from_dict(data_class=classes.GetInfoResult, data=data)
    
  def getVersion(self):
    data = self.send(method=methods.GetVersion)
    return str(data)
  
  def getHeight(self):
    data = self.send(method=methods.GetHeight)
    return int(data)
  
  def getTopoheight(self):
    data = self.send(method=methods.GetTopoheight)
    return int(data)
  
  def getStableheight(self):
    data = self.send(method=methods.GetStableheight)
    return int(data)
    
  def getBlockTemplate(self, address: str):
    data = self.send(method=methods.GetBlockTemplate, params={ "address": address })
    return from_dict(data_class=classes.GetBlockTemplateResult, data=data)
    
  def getBlockAtTopoheight(self, params: classes.GetBlockAtTopoheightParams):
    data = self.send(method=methods.GetBlockAtTopoheight, params=vars(params))
    return from_dict(data_class=classes.Block, data=data)
  
  def getBlocksAtHeight(self, params: classes.GetBlocksAtHeightParams):
    data = self.send(method=methods.GetBlocksAtHeight, params=vars(params))
    items = [from_dict(data_class=classes.Block, data=item) for item in data]
    return items