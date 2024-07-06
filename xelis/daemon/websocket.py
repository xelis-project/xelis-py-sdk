from typing import Optional
from websockets.client import connect, WebSocketClientProtocol
from daemon import classes, events, methods
from rpc.websocket import RPCWS

async def ConnectDaemonWS(url: str):
  client = await connect(uri=url)
  return DaemonWS(client=client)

class DaemonWS(RPCWS):
  async def getInfo(self):
    data = await self.send(method=methods.GetInfo)
    return classes.GetInfoResult.from_dict(d=data)
    
  async def getVersion(self):
    data = await self.send(method=methods.GetVersion)
    return str(data)
  
  async def getHeight(self):
    data = await self.send(method=methods.GetHeight)
    return int(data)
  
  async def getTopoheight(self):
    data = await self.send(method=methods.GetTopoheight)
    return int(data)
  
  async def getStableHeight(self):
    data = await self.send(method=methods.GetStableHeight)
    return int(data)
    
  async def getBlockTemplate(self, address: str):
    data = await self.send(method=methods.GetBlockTemplate, params={ "address": address })
    return classes.GetBlockTemplateResult.from_dict(d=data)
    
  async def getBlockAtTopoheight(self, params: classes.GetBlockAtTopoheightParams):
    data = await self.send(method=methods.GetBlockAtTopoheight, params=params.to_dict())
    return classes.Block.from_dict(d=data)
  
  async def getBlocksAtHeight(self, params: classes.GetBlocksAtHeightParams):
    data = await self.send(method=methods.GetBlocksAtHeight, params=params.to_dict())
    items = [classes.Block.from_dict(d=item) for item in data]
    return items
  
  async def getBlockByHash(self, params: classes.GetBlockByHashParams):
    data = await self.send(method=methods.GetBlockByHash, params=params.to_dict())
    return classes.Block.from_dict(d=data)
  
  async def getTopBlock(self, params: classes.GetTopBlockParams):
    data = await self.send(method=methods.GetTopBlock, params=params.to_dict())
    return classes.Block.from_dict(d=data)
  
  async def getNonce(self, address: str):
    data = await self.send(method=methods.GetNonce, params={ "address": address })
    return classes.GetNonceResult.from_dict(d=data)
  
  async def hasNonce(self, address: str):
    data = await self.send(method=methods.HasNonce, params={ "address": address })
    exist = data["exist"]
    return bool(exist)
  
  async def getNonceAtTopoheight(self, params: classes.GetNonceAtTopoheightParams):
    data = await self.send(method=methods.GetNonceAtTopoheight, params=params.to_dict())
    return classes.VersionedNonce.from_dict(d=data)
  
  async def getBalance(self, params: classes.GetBalanceParams):
    data = await self.send(method=methods.GetBalance, params=params.to_dict())
    return classes.GetBalanceResult.from_dict(d=data)
  
  async def getStableBalance(self, params: classes.GetBalanceParams):
    data = await self.send(method=methods.GetStableBalance, params=params.to_dict())
    return classes.GetStableBalanceResult.from_dict(d=data)

  async def hasBalance(self, params: classes.GetBalanceParams):
    data = await self.send(method=methods.HasBalance, params=params.to_dict())
    exist = data["exist"]
    return bool(exist)
  
  async def getBalanceAtTopoheight(self, params: classes.GetBalanceAtTopoheightParams):
    data = await self.send(method=methods.GetBalanceAtTopoheight, params=params.to_dict())
    return classes.VersionedBalance.from_dict(d=data)
  
  async def getAsset(self, asset: str):
    data = await self.send(method=methods.GetAsset, params={ "asset": asset })
    return classes.Asset.from_dict(d=data)
  
  async def getAssets(self, params: str):
    data = await self.send(method=methods.GetAssets, params=params.to_dict())
    items = [classes.AssetWithData.from_dict(d=item) for item in data]
    return items
  
  async def countAssets(self):
    data = await self.send(method=methods.CountAssets)
    return int(data)
  
  async def countTransactions(self):
    data = await self.send(method=methods.CountTransactions)
    return int(data)
  
  async def countAccounts(self):
    data = await self.send(method=methods.CountAccounts)
    return int(data)
  
  async def getTips(self):
    data = await self.send(method=methods.GetTips)
    items = [str(item) for item in data]
    return items
  
  async def p2pStatus(self):
    data = await self.send(method=methods.P2PStatus)
    return classes.P2PStatusResult.from_dict(d=data)
  
  async def getDAGOrder(self, params: classes.GetTopoheightRangeParams):
    data = await self.send(method=methods.GetDAGOrder, params=params.to_dict())
    items = [str(item) for item in data]
    return items
  
  async def submitBlock(self, params: classes.SubmitBlockParams):
    data = await self.send(method=methods.SubmitBlock, params=params.to_dict())
    return bool(data)
  
  async def submitTransaction(self, hexData: str):
    data = await self.send(method=methods.SubmitTransaction, params={ "data": hexData })
    return bool(data)
  
  async def getMempool(self):
    data = await self.send(method=methods.GetMempool)
    items = [classes.Transaction.from_dict(d=item) for item in data]
    return items
  
  async def getTransaction(self, hash: str):
    data = await self.send(method=methods.GetTransaction, params={ "hash": hash })
    return classes.Transaction.from_dict(d=data)
  
  async def getTransactions(self, params: classes.GetTransactionsParams):
    data = await self.send(method=methods.GetTransactions, params=params.to_dict())
    items = [classes.Transaction.from_dict(d=item) for item in data]
    return items
  
  async def getBlocksRangeByTopoheight(self, params: classes.GetTopoheightRangeParams):
    data = await self.send(method=methods.GetBlocksRangeByTopoheight, params=params.to_dict())
    items = [classes.Block.from_dict(d=item) for item in data]
    return items
  
  async def getBlocksRangeByHeight(self, params: classes.GetHeightRangeParams):
    data = await self.send(method=methods.GetBlocksRangeByHeight, params=params.to_dict())
    items = [classes.Block.from_dict(d=item) for item in data]
    return items
  
  async def getAccounts(self, params: classes.GetAssetsParams):
    data = await self.send(method=methods.GetAccounts, params=params.to_dict())
    items = [str(item) for item in data]
    return items
  
  async def getAccountHistory(self, address: str):
    data = await self.send(method=methods.GetAccountHistory, params={ "address": address })
    items = [classes.AccountHistory.from_dict(d=item) for item in data]
    return items

  async def getAccountAssets(self, address: str):
    data = await self.send(method=methods.GetAccountAssets, params={ "address": address })
    items = [str(item) for item in data]
    return items

  async def getPeers(self):
    data = await self.send(method=methods.GetPeers)
    return classes.GetPeersResult.from_dict(data)

  async def getDevFeeThresholds(self):
    data = await self.send(method=methods.GetDevFeeThresholds)
    items = [classes.Fee.from_dict(item) for item in data]
    return items
  
  async def getSizeOnDisk(self):
    data = await self.send(method=methods.GetSizeOnDisk)
    return classes.SizeOnDisk.from_dict(data)
  
  async def isTxExecutedInBlock(self, params: classes.IsTxExecutedInBlockParams):
    data = await self.send(method=methods.IsTxExecutedInBlock, params=params.to_dict())
    return bool(data)
  
  async def getAccountRegistrationTopoheight(self, address: str):
    data = await self.send(method=methods.GetAccountRegistrationTopoheight, params={ "address": address })
    return int(data)
  
  async def isAccountRegistered(self, params: classes.IsAccountRegisteredParams):
    data = await self.send(method=methods.IsAccountRegistered, params=params.to_dict())
    return bool(data)
  
  async def getDifficulty(self):
    data = await self.send(method=methods.GetDifficulty)
    return classes.GetDifficultyResult.from_dict(d=data)
  
  async def validateAddress(self, params: classes.ValidateAddressParams):
    data = await self.send(method=methods.ValidateAddress, params=params.to_dict())
    return classes.ValidateAddressResult.from_dict(data)
  
  async def extractKeyFromAddress(self, params: classes.ExtractKeyFromAddressParams):
    data = await self.send(method=methods.ExtractKeyFromAddress, params=params.to_dict())
    return data
  
  async def createMinerWork(self, params: classes.CreateMinerWorkParams):
    data = await self.send(method=methods.CreateMinerWork, params=params.to_dict())
    return classes.CreateMinerWorkResult.from_dict(data)
  
  async def onNewBlock(self):
    result = await self.listenEvent(events.NewBlock)
    if result is not None:
      return classes.Block.from_dict(result)
    
  async def onTransactionAddedInMempool(self):
    result = await self.listenEvent(events.TransactionAddedInMempool)
    if result is not None:
      return classes.Transaction.from_dict(result)
    
  async def onTransactionExecuted(self):
    result = await self.listenEvent(events.TransactionExecuted)
    if result is not None:
      return classes.TransactionExecutedResult.from_dict(result)
    
  async def onBlockOrdered(self):
    result = await self.listenEvent(events.BlockOrdered)
    if result is not None:
      return classes.Block.from_dict(result)
    
  async def onPeerConnected(self):
    result = await self.listenEvent(events.PeerConnected)
    if result is not None:
      return classes.Peer.from_dict(result)
    
  async def onPeerDisconnected(self):
    result = await self.listenEvent(events.PeerDisconnected)
    if result is not None:
      return int(result)

  async def onPeerStateUpdated(self):
    result = await self.listenEvent(events.PeerStateUpdated)
    if result is not None:
      return classes.Peer.from_dict(result)