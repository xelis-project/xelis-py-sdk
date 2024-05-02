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
  
  def getBlockByHash(self, params: classes.GetBlockByHashParams):
    data = self.fetch(method=methods.GetBlockByHash, params=vars(params))
    return from_dict(data_class=classes.Block, data=data)
  
  def getTopBlock(self, params: classes.GetTopBlockParams):
    data = self.fetch(method=methods.GetTopBlock, params=vars(params))
    return from_dict(data_class=classes.Block, data=data)
  
  def getNonce(self, address: str):
    data = self.fetch(method=methods.GetNonce, params={ "address": address })
    return from_dict(data_class=classes.GetNonceResult, data=data)
  
  def hasNonce(self, address: str):
    data = self.fetch(method=methods.HasNonce, params={ "address": address })
    exist = data["exist"]
    return bool(exist)
  
  def getNonceAtTopoheight(self, params: classes.GetNonceAtTopoheightParams):
    data = self.fetch(method=methods.GetNonceAtTopoheight, params=vars(params))
    return from_dict(data_class=classes.VersionedNonce, data=data)
  
  def getBalance(self, params: classes.GetBalanceParams):
    data = self.fetch(method=methods.GetBalance, params=vars(params))
    return from_dict(data_class=classes.GetBalanceResult, data=data)
  
  def hasBalance(self, params: classes.GetBalanceParams):
    data = self.fetch(method=methods.HasBalance, params=vars(params))
    exist = data["exist"]
    return bool(exist)
  
  def getBalanceAtTopoheight(self, params: classes.GetBalanceAtTopoheightParams):
    data = self.fetch(method=methods.GetBalanceAtTopoheight, params=vars(params))
    return from_dict(data_class=classes.VersionedBalance, data=data)