from websockets.sync.client import connect, ClientConnection
from rpc.websocket import RPCWS
from wallet import classes, methods
from rpc.util import createBasicAuthToken

class WalletWS(RPCWS):
  def __init__(self, client: ClientConnection = None, url: str = None, username: str = None, password: str = None) -> None:
    if url is not None:
      authToken = createBasicAuthToken(username=username, password=password)
      client = connect(uri=url, additional_headers={ "Authorization": authToken })

    super().__init__(client)
  
  def getVersion(self):
    data = self.send(method=methods.GetVersion)
    return str(data)
  
  def getNetwork(self):
    data = self.send(method=methods.GetNetwork)
    return str(data)
  
  def getNonce(self):
    data = self.send(method=methods.GetNonce)
    return int(data)
  
  def getTopoheight(self):
    data = self.send(method=methods.GetTopoheight)
    return int(data)
  
  def getAddress(self, params: classes.GetAddressParams):
    data = self.send(method=methods.GetAddress, params=params.to_dict())
    return str(data)
  
  def splitAddress(self, params: classes.SplitAddressParams):
    data = self.send(method=methods.SplitAddress, params=params.to_dict())
    return classes.SplitAddressResult.from_dict(data)
  
  def rescan(self, params: classes.RescanParams):
    data = self.send(method=methods.Rescan, params=params.to_dict())
    return bool(data)
  
  def getBalance(self, params: classes.GetBalanceParams):
    data = self.send(method=methods.GetBalance, params=params.to_dict())
    return int(data)
  
  def hasBalance(self, params: classes.GetBalanceParams):
    data = self.send(method=methods.HasBalance, params=params.to_dict())
    return bool(data)
  
  def getTrackedAssets(self):
    data = self.send(method=methods.GetTrackedAssets)
    items = [str(item) for item in data]
    return items
  
  def getAssetPrecision(self, params: classes.GetBalanceParams):
    data = self.send(method=methods.GetAssetPrecision, params=params.to_dict())
    return int(data)
  
  def getTransaction(self, hash: str):
    data = self.send(method=methods.GetTransaction, params={ "hash": hash })
    return classes.TransactionEntry.from_dict(data)
  
  def buildTransaction(self, params: classes.BuildTransactionParams):
    data = self.send(method=methods.BuildTransaction, params=params.to_dict())
    return classes.BuildTransactionResult.from_dict(data)
  
  def listTransactions(self, params: classes.ListTransactionsParams):
    data = self.send(method=methods.ListTransactions, params=params.to_dict())
    items = [classes.TransactionEntry.from_dict(item) for item in data]
    return items
  
  def isOnline(self):
    data = self.send(method=methods.IsOnline)
    return bool(data)
  
  def setOnlineMode(self, params: classes.SetOnlineModeParams):
    data = self.send(method=methods.SetOnlineMode, params=params.to_dict())
    return bool(data)
  
  def setOfflineMode(self):
    data = self.send(method=methods.SetOfflineMode)
    return bool(data)
  
  def signData(self, data: any):
    signature = self.send(method=methods.SignData, params=data)
    return str(signature)
  
  def estimateFees(self, params: classes.EstimateFeesParams):
    data = self.send(method=methods.EstimateFees, params=params.to_dict())
    return int(data)