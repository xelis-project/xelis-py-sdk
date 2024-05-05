from websockets.sync.client import connect, ClientConnection
from daemon import classes, methods
from rpc.websocket import RPCWS

class DaemonWS(RPCWS):
  def __init__(self, client: ClientConnection = None, url: str = None) -> None:
    if url is not None:
      client = connect(uri=url)

    super().__init__(client)
    
  def getInfo(self):
    data = self.send(method=methods.GetInfo)
    return classes.GetInfoResult.from_dict(d=data)
    
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
    return classes.GetBlockTemplateResult.from_dict(d=data)
    
  def getBlockAtTopoheight(self, params: classes.GetBlockAtTopoheightParams):
    data = self.send(method=methods.GetBlockAtTopoheight, params=params.to_dict())
    return classes.Block.from_dict(d=data)
  
  def getBlocksAtHeight(self, params: classes.GetBlocksAtHeightParams):
    data = self.send(method=methods.GetBlocksAtHeight, params=params.to_dict())
    items = [classes.Block.from_dict(d=item) for item in data]
    return items
  
  def getBlockByHash(self, params: classes.GetBlockByHashParams):
    data = self.send(method=methods.GetBlockByHash, params=params.to_dict())
    return classes.Block.from_dict(d=data)
  
  def getTopBlock(self, params: classes.GetTopBlockParams):
    data = self.send(method=methods.GetTopBlock, params=params.to_dict())
    return classes.Block.from_dict(d=data)
  
  def getNonce(self, address: str):
    data = self.send(method=methods.GetNonce, params={ "address": address })
    return classes.GetNonceResult.from_dict(d=data)
  
  def hasNonce(self, address: str):
    data = self.send(method=methods.HasNonce, params={ "address": address })
    exist = data["exist"]
    return bool(exist)
  
  def getNonceAtTopoheight(self, params: classes.GetNonceAtTopoheightParams):
    data = self.send(method=methods.GetNonceAtTopoheight, params=params.to_dict())
    return classes.VersionedNonce.from_dict(d=data)
  
  def getBalance(self, params: classes.GetBalanceParams):
    data = self.send(method=methods.GetBalance, params=params.to_dict())
    return classes.GetBalanceResult.from_dict(d=data)
  
  def hasBalance(self, params: classes.GetBalanceParams):
    data = self.send(method=methods.HasBalance, params=params.to_dict())
    exist = data["exist"]
    return bool(exist)
  
  def getBalanceAtTopoheight(self, params: classes.GetBalanceAtTopoheightParams):
    data = self.send(method=methods.GetBalanceAtTopoheight, params=params.to_dict())
    return classes.VersionedBalance.from_dict(d=data)
  
  def getAsset(self, asset: str):
    data = self.send(method=methods.GetAsset, params={ "asset": asset })
    return classes.Asset.from_dict(d=data)
  
  def getAssets(self, params: str):
    data = self.send(method=methods.GetAssets, params=params.to_dict())
    items = [classes.AssetWithData.from_dict(d=item) for item in data]
    return items
  
  def countAssets(self):
    data = self.send(method=methods.CountAssets)
    return int(data)
  
  def countTransactions(self):
    data = self.send(method=methods.CountTransactions)
    return int(data)
  
  def countAccounts(self):
    data = self.send(method=methods.CountAccounts)
    return int(data)
  
  def getTips(self):
    data = self.send(method=methods.GetTips)
    items = [str(item) for item in data]
    return items
  
  def p2pStatus(self):
    data = self.send(method=methods.P2PStatus)
    return classes.P2PStatusResult.from_dict(d=data)
  
  def getDAGOrder(self, params: classes.GetTopoheightRangeParams):
    data = self.send(method=methods.GetDAGOrder, params=params.to_dict())
    items = [str(item) for item in data]
    return items
  
  def submitBlock(self, params: classes.SubmitBlockParams):
    data = self.send(method=methods.SubmitBlock, params=params.to_dict())
    return bool(data)
  
  def submitTransaction(self, hexData: str):
    data = self.send(method=methods.SubmitTransaction, params={ "data": hexData })
    return bool(data)
  
  def getMempool(self):
    data = self.send(method=methods.GetMempool)
    items = [classes.Transaction.from_dict(d=item) for item in data]
    return items
  
  def getTransaction(self, hash: str):
    data = self.send(method=methods.GetTransaction, params={ "hash": hash })
    return classes.Transaction.from_dict(d=data)
  
  def getTransactions(self, params: classes.GetTransactionsParams):
    data = self.send(method=methods.GetTransactions, params=params.to_dict())
    items = [classes.Transaction.from_dict(d=item) for item in data]
    return items
  
  def getBlocksRangeByTopoheight(self, params: classes.GetTopoheightRangeParams):
    data = self.send(method=methods.GetBlocksRangeByTopoheight, params=params.to_dict())
    items = [classes.Block.from_dict(d=item) for item in data]
    return items
  
  def getBlocksRangeByHeight(self, params: classes.GetHeightRangeParams):
    data = self.send(method=methods.GetBlocksRangeByHeight, params=params.to_dict())
    items = [classes.Block.from_dict(d=item) for item in data]
    return items
  
  def getAccounts(self, params: classes.GetAssetsParams):
    data = self.send(method=methods.GetAccounts, params=params.to_dict())
    items = [str(item) for item in data]
    return items
  
  def getAccountHistory(self, address: str):
    data = self.send(method=methods.GetAccountHistory, params={ "address": address })
    items = [classes.AccountHistory.from_dict(d=item) for item in data]
    return items

  def getAccountAssets(self, address: str):
    data = self.send(method=methods.GetAccountAssets, params={ "address": address })
    items = [str(item) for item in data]
    return items

  def getPeers(self):
    data = self.send(method=methods.GetPeers)
    return classes.GetPeersResult.from_dict(data)

  def getDevFeeThresholds(self):
    data = self.send(method=methods.GetDevFeeThresholds)
    items = [classes.Fee.from_dict(item) for item in data]
    return items
  
  def getSizeOnDisk(self):
    data = self.send(method=methods.GetSizeOnDisk)
    return classes.SizeOnDisk.from_dict(data)
  
  def isTxExecutedInBlock(self, params: classes.IsTxExecutedInBlockParams):
    data = self.send(method=methods.IsTxExecutedInBlock, params=params.to_dict())
    return bool(data)
  
  def getAccountRegistrationTopoheight(self, address: str):
    data = self.send(method=methods.GetAccountRegistrationTopoheight, params={ "address": address })
    return int(data)
  
  def isAccountRegistered(self, params: classes.IsAccountRegisteredParams):
    data = self.send(method=methods.IsAccountRegistered, params=params.to_dict())
    return bool(data)
  
  def getDifficulty(self):
    data = self.send(method=methods.GetDifficulty)
    return classes.GetDifficultyResult.from_dict(d=data)
  
    
  def validateAddress(self, params: classes.ValidateAddressParams):
    data = self.send(method=methods.ValidateAddress, params=params.to_dict())
    return bool(data)
  
  def extractKeyFromAddress(self, params: classes.ExtractKeyFromAddressParams):
    data = self.send(method=methods.ExtractKeyFromAddress, params=params.to_dict())
    return data
  
  def createMinerWork(self, params: classes.CreateMinerWorkParams):
    data = self.send(method=methods.CreateMinerWork, params=params.to_dict())
    return classes.CreateMinerWorkResult.from_dict(data)