import daemon.methods as methods
import daemon.classes as classes
from rpc.http import RPCHttp

class DaemonRPC(RPCHttp):
  def getInfo(self) -> classes.GetInfoResult:
    data = self.fetch(method=methods.GetInfo)
    return classes.GetInfoResult.from_dict(d=data)
  
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
    return classes.GetBlockTemplateResult.from_dict(d=data)
  
  def getBlockAtTopoheight(self, params: classes.GetBlockAtTopoheightParams):
    data = self.fetch(method=methods.GetBlockAtTopoheight, params=vars(params))
    return classes.Block.from_dict(d=data)
  
  def getBlocksAtHeight(self, params: classes.GetBlocksAtHeightParams):
    data = self.fetch(method=methods.GetBlocksAtHeight, params=vars(params))
    items = [classes.Block.from_dict(d=item) for item in data]
    return items
  
  def getBlockByHash(self, params: classes.GetBlockByHashParams):
    data = self.fetch(method=methods.GetBlockByHash, params=vars(params))
    return classes.Block.from_dict(d=data)
  
  def getTopBlock(self, params: classes.GetTopBlockParams):
    data = self.fetch(method=methods.GetTopBlock, params=vars(params))
    return classes.Block.from_dict(d=data)
  
  def getNonce(self, address: str):
    data = self.fetch(method=methods.GetNonce, params={ "address": address })
    return classes.GetNonceResult.from_dict(d=data)
  
  def hasNonce(self, address: str):
    data = self.fetch(method=methods.HasNonce, params={ "address": address })
    exist = data["exist"]
    return bool(exist)
  
  def getNonceAtTopoheight(self, params: classes.GetNonceAtTopoheightParams):
    data = self.fetch(method=methods.GetNonceAtTopoheight, params=vars(params))
    return classes.VersionedNonce.from_dict(d=data)
  
  def getBalance(self, params: classes.GetBalanceParams):
    data = self.fetch(method=methods.GetBalance, params=vars(params))
    return classes.GetBalanceResult.from_dict(d=data)
  
  def hasBalance(self, params: classes.GetBalanceParams):
    data = self.fetch(method=methods.HasBalance, params=vars(params))
    exist = data["exist"]
    return bool(exist)
  
  def getBalanceAtTopoheight(self, params: classes.GetBalanceAtTopoheightParams):
    data = self.fetch(method=methods.GetBalanceAtTopoheight, params=vars(params))
    return classes.VersionedBalance.from_dict(d=data)
  
  def getAsset(self, asset: str):
    data = self.fetch(method=methods.GetAsset, params={ "asset": asset })
    return classes.Asset.from_dict(d=data)
  
  def getAssets(self, params: classes.GetAssetsParams):
    data = self.fetch(method=methods.GetAssets, params=vars(params))
    items = [classes.AssetWithData.from_dict(d=item) for item in data]
    return items
  
  def countAssets(self):
    data = self.fetch(method=methods.CountAssets)
    return int(data)
  
  def countTransactions(self):
    data = self.fetch(method=methods.CountTransactions)
    return int(data)
  
  def countAccounts(self):
    data = self.fetch(method=methods.CountAccounts)
    return int(data)

  def getTips(self):
    data = self.fetch(method=methods.GetTips)
    items = [str(item) for item in data]
    return items
  
  def p2pStatus(self):
    data = self.fetch(method=methods.P2PStatus)
    return classes.P2PStatusResult.from_dict(d=data)
  
  def getDAGOrder(self, params: classes.GetTopoheightRangeParams):
    data = self.fetch(method=methods.GetDAGOrder, params=vars(params))
    items = [str(item) for item in data]
    return items
  
  def submitBlock(self, params: classes.SubmitBlockParams):
    data = self.fetch(method=methods.SubmitBlock, params=vars(params))
    return bool(data)
  
  def submitTransaction(self, hexData: str):
    data = self.fetch(method=methods.SubmitTransaction, params={ "data": hexData })
    return bool(data)
  
  def getMempool(self):
    data = self.fetch(method=methods.GetMempool)
    items = [classes.Transaction.from_dict(d=item) for item in data]
    return items
  
  def getTransaction(self, hash: str):
    data = self.fetch(method=methods.GetTransaction, params={ "hash": hash })
    return classes.Transaction.from_dict(d=data)
  
  def getTransactions(self, params: classes.GetTransactionsParams):
    data = self.fetch(method=methods.GetTransactions, params=vars(params))
    items = [classes.Transaction.from_dict(d=item) for item in data]
    return items
  
  def getBlocksRangeByTopoheight(self, params: classes.GetTopoheightRangeParams):
    data = self.fetch(method=methods.GetBlocksRangeByTopoheight, params=vars(params))
    items = [classes.Block.from_dict(d=item) for item in data]
    return items
  
  def getBlocksRangeByHeight(self, params: classes.GetHeightRangeParams):
    data = self.fetch(method=methods.GetBlocksRangeByHeight, params=vars(params))
    items = [classes.Block.from_dict(d=item) for item in data]
    return items
  
  def getAccounts(self, params: classes.GetAssetsParams):
    data = self.fetch(method=methods.GetAccounts, params=vars(params))
    items = [str(item) for item in data]
    return items
  
  def getAccountHistory(self, address: str):
    data = self.fetch(method=methods.GetAccountHistory, params={ "address": address })
    items = [classes.AccountHistory.from_dict(d=item) for item in data]
    return items

  def getAccountAssets(self, address: str):
    data = self.fetch(method=methods.GetAccountAssets, params={ "address": address })
    items = [str(item) for item in data]
    return items
  
  def getPeers(self):
    data = self.fetch(method=methods.GetPeers)
    return classes.GetPeersResult.from_dict(d=data)

  def getDevFeeThresholds(self):
    data = self.fetch(method=methods.GetDevFeeThresholds)
    items = [classes.Fee.from_dict(d=item) for item in data]
    return items
  
  def getSizeOnDisk(self):
    data = self.fetch(method=methods.GetSizeOnDisk)
    return classes.SizeOnDisk.from_dict(d=data)
  
  def isTxExecutedInBlock(self, params: classes.IsTxExecutedInBlockParams):
    data = self.fetch(method=methods.IsTxExecutedInBlock, params=vars(params))
    return bool(data)
  
  def getAccountRegistrationTopoheight(self, address: str):
    data = self.fetch(method=methods.GetAccountRegistrationTopoheight, params={ "address": address })
    return int(data)
  
  def isAccountRegistered(self, params: classes.IsAccountRegisteredParams):
    data = self.fetch(method=methods.IsAccountRegistered, params=vars(params))
    return bool(data)
  
  def getDifficulty(self):
    data = self.fetch(method=methods.GetDifficulty)
    return classes.GetDifficultyResult.from_dict(d=data)
  
  def validateAddress(self, params: classes.ValidateAddressParams):
    data = self.fetch(method=methods.ValidateAddress, params=vars(params))
    return bool(data)
  
  def extractKeyFromAddress(self, params: classes.ExtractKeyFromAddressParams) -> str | list[int]:
    data = self.fetch(method=methods.ExtractKeyFromAddress, params=vars(params))
    return data
  
  def createMinerWork(self, params: classes.CreateMinerWorkParams):
    data = self.fetch(method=methods.CreateMinerWork, params=vars(params))
    return classes.CreateMinerWorkResult.from_dict(data)