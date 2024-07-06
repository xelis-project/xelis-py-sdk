from websockets.client import connect
import daemon.classes as daemonClasses
from rpc.websocket import RPCWS
from wallet import classes, methods, events
from rpc.util import createBasicAuthToken

async def ConnectWalletWS(url: str, username: str, password: str):
  authToken = createBasicAuthToken(username=username, password=password)
  client = await connect(uri=url, extra_headers={ "Authorization": authToken })
  return WalletWS(client=client)

class WalletWS(RPCWS):
  async def getVersion(self):
    data = await self.send(method=methods.GetVersion)
    return str(data)
  
  async def getNetwork(self):
    data = await self.send(method=methods.GetNetwork)
    return str(data)
  
  async def getNonce(self):
    data = await self.send(method=methods.GetNonce)
    return int(data)
  
  async def getTopoheight(self):
    data = await self.send(method=methods.GetTopoheight)
    return int(data)
  
  async def getAddress(self, params: classes.GetAddressParams):
    data = await self.send(method=methods.GetAddress, params=params.to_dict())
    return str(data)
  
  async def splitAddress(self, params: classes.SplitAddressParams):
    data = await self.send(method=methods.SplitAddress, params=params.to_dict())
    return classes.SplitAddressResult.from_dict(data)
  
  async def rescan(self, params: classes.RescanParams):
    data = await self.send(method=methods.Rescan, params=params.to_dict())
    return bool(data)
  
  async def getBalance(self, params: classes.GetBalanceParams):
    data = await self.send(method=methods.GetBalance, params=params.to_dict())
    return int(data)
  
  async def hasBalance(self, params: classes.GetBalanceParams):
    data = await self.send(method=methods.HasBalance, params=params.to_dict())
    return bool(data)
  
  async def getTrackedAssets(self):
    data = await self.send(method=methods.GetTrackedAssets)
    items = [str(item) for item in data]
    return items
  
  async def getAssetPrecision(self, params: classes.GetBalanceParams):
    data = await self.send(method=methods.GetAssetPrecision, params=params.to_dict())
    return int(data)
  
  async def getTransaction(self, hash: str):
    data = await self.send(method=methods.GetTransaction, params={ "hash": hash })
    return classes.TransactionEntry.from_dict(data)
  
  async def buildTransaction(self, params: classes.BuildTransactionParams):
    data = await self.send(method=methods.BuildTransaction, params=params.to_dict())
    return classes.BuildTransactionResult.from_dict(data)
  
  async def listTransactions(self, params: classes.ListTransactionsParams):
    data = await self.send(method=methods.ListTransactions, params=params.to_dict())
    items = [classes.TransactionEntry.from_dict(item) for item in data]
    return items
  
  async def isOnline(self):
    data = await self.send(method=methods.IsOnline)
    return bool(data)
  
  async def setOnlineMode(self, params: classes.SetOnlineModeParams):
    data = await self.send(method=methods.SetOnlineMode, params=params.to_dict())
    return bool(data)
  
  async def setOfflineMode(self):
    data = await self.send(method=methods.SetOfflineMode)
    return bool(data)
  
  async def signData(self, data: any):
    signature = await self.send(method=methods.SignData, params=data)
    return str(signature)
  
  async def estimateFees(self, params: classes.EstimateFeesParams):
    data = await self.send(method=methods.EstimateFees, params=params.to_dict())
    return int(data)
  
  async def onBalanceChanged(self):
    result = await self.listenEvent(events.BalanceChanged)
    if result is not None:
      return classes.BalanceChangedResult.from_dict(result)
    
  async def onNewAsset(self):
    result = await self.listenEvent(events.NewAsset)
    if result is not None:
      return daemonClasses.AssetWithData.from_dict(result)
    
  async def onNewTopoheight(self):
    result = await self.listenEvent(events.NewTopoHeight)
    if result is not None:
      return int(result["topoheight"])
    
  async def onNewTransaction(self):
    result = await self.listenEvent(events.NewTransaction)
    if result is not None:
      return classes.TransactionEntry.from_dict(result)
    
  async def onOffline(self):
    result = await self.listenEvent(events.Offline)
    if result is not None:
      return bool(result)
    
  async def onOnline(self):
    result = await self.listenEvent(events.Online)
    if result is not None:
      return bool(result)
    
  async def onRescan(self):
    result = await self.listenEvent(events.Rescan)
    if result is not None:
      return int(result["start_topoheight"])