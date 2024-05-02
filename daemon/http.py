from dacite import from_dict
import daemon.methods as methods
import daemon.classes as classes
from rpc.http import RPCHttp

class DaemonRPC(RPCHttp):
  def getInfo(self) -> classes.GetInfoResult:
    data = self.fetch(method=methods.GetInfo)
    return from_dict(data_class=classes.GetInfoResult, data=data)
  
  def getVersion(self) -> str:
    data = self.fetch(method=methods.GetVersion)
    return str(data)
  
  def getHeight(self) -> int:
    data = self.fetch(method=methods.GetHeight)
    return int(data)
  
  def getTopoheight(self) -> int:
    data = self.fetch(method=methods.GetTopoheight)
    return int(data)
  
  def getStableheight(self) -> int:
    data = self.fetch(method=methods.GetStableheight)
    return int(data)
  
  def getBlockTemplate(self, address: str):
    data = self.fetch(method=methods.GetBlockTemplate, params={ "address": address })
    return from_dict(data_class=classes.GetBlockTemplateResult, data=data)
  
  def getBlockAtTopoheight(self, params: classes.GetBlockAtTopoheightParams):
    data = self.fetch(method=methods.GetBlockAtTopoheight, params=vars(params))
    return from_dict(data_class=classes.Block, data=data)
  
  def getBlocksAtHeight(self, params: classes.GetBlocksAtHeightParams):
    data = self.fetch(method=methods.GetBlocksAtHeight, params=vars(params))
    items = [from_dict(data_class=classes.Block, data=item) for item in data]
    return items