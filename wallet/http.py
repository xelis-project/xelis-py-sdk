from rpc.http import RPCHttp
from wallet import classes, methods
from rpc.util import createBasicAuthToken

class WalletRPC(RPCHttp):
  authToken: str
  
  def __init__(self, url: str, username: str, password: str) -> None:
    self.authToken = createBasicAuthToken(username=username, password=password)
    super().__init__(url)
  
  def fetch(self, method: str, params=None):
    return super().fetch(method, params, { "Authorization": self.authToken })
  
  def getVersion(self):
    data = self.fetch(method=methods.GetVersion)
    return str(data)
  
  def getNetwork(self):
    data = self.fetch(method=methods.GetNetwork)
    return str(data)
  
  def getNonce(self):
    data = self.fetch(method=methods.GetNonce)
    return int(data)
  
  def getTopoheight(self):
    data = self.fetch(method=methods.GetTopoheight)
    return int(data)
  
  def getAddress(self, params: classes.GetAddressParams):
    data = self.fetch(method=methods.GetAddress, params=vars(params))
    return str(data)
  
  def splitAddress(self, params: classes.SplitAddressParams):
    data = self.fetch(method=methods.SplitAddress, params=vars(params))
    return classes.SplitAddressResult.from_dict(data)
  
  def rescan(self, params: classes.RescanParams):
    data = self.fetch(method=methods.Rescan, params=vars(params))
    return bool(data)
  
  def getBalance(self, params: classes.GetBalanceParams):
    data = self.fetch(method=methods.GetBalance, params=vars(params))
    return int(data)
  
  def hasBalance(self, params: classes.GetBalanceParams):
    data = self.fetch(method=methods.HasBalance, params=vars(params))
    return bool(data)
  
  def getTrackedAssets(self):
    data = self.fetch(method=methods.GetTrackedAssets)
    items = [str(item) for item in data]
    return items
  
  def getAssetPrecision(self, params: classes.GetBalanceParams):
    data = self.fetch(method=methods.GetAssetPrecision, params=vars(params))
    return int(data)
  
  def getTransaction(self, hash: str):
    data = self.fetch(method=methods.GetTransaction, params={ "hash": hash })
    return classes.TransactionEntry.from_dict(data)
  
  def buildTransaction(self, params: classes.BuildTransactionParams):
    data = self.fetch(method=methods.BuildTransaction, params=vars(params))
    return classes.BuildTransactionResult.from_dict(data)
  
  def listTransactions(self, params: classes.ListTransactionsParams):
    data = self.fetch(method=methods.ListTransactions, params=vars(params))
    items = [classes.TransactionEntry.from_dict(item) for item in data]
    return items
  
  def isOnline(self):
    data = self.fetch(method=methods.IsOnline)
    return bool(data)
  
  def setOnlineMode(self):
    data = self.fetch(method=methods.SetOnlineMode)
    return bool(data)
  
  def setOfflineMode(self):
    data = self.fetch(method=methods.SetOfflineMode)
    return bool(data)
  
  def signData(self, data: any):
    signature = self.fetch(method=methods.SignData, params=data)
    return str(signature)
  
  def estimateFees(self, params: classes.EstimateFeesParams):
    data = self.fetch(method=methods.EstimateFees, params=params)
    return int(data)