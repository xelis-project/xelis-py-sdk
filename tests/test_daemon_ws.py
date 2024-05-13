import asyncio
import pytest
from config.module import TESTNET_NODE_WS, XELIS_ASSET, MAINNET_NODE_WS
from daemon import events
from daemon.websocket import ConnectDaemonWS, DaemonWS
import daemon.classes as classes

TESTNET_ADDR = "xet:rsdm79np9eqar7cg5jy9sdhwas74l4ml5enaasmae8jtjcvpr3vqqnlpysy"

@pytest.mark.asyncio
async def test_getInfo():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getInfo()
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getVersion():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getVersion()
  print(data)
  await daemon.close()
    
@pytest.mark.asyncio
async def test_getHeight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getHeight()
  print(data)
  await daemon.close()
    
@pytest.mark.asyncio
async def test_getTopoheight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getTopoheight()
  print(data)
  await daemon.close()
    
@pytest.mark.asyncio
async def test_getStableheight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getStableheight()
  print(data)
  await daemon.close()
    
@pytest.mark.asyncio
async def test_getBlockTemplate():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getBlockTemplate(address=TESTNET_ADDR)
  print(data)
  await daemon.close()
    
@pytest.mark.asyncio
async def test_getBlockAtTopoheight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getBlockAtTopoheight(classes.GetBlockAtTopoheightParams(topoheight=0, include_txs=False))
  print(data)
  await daemon.close()
    
@pytest.mark.asyncio
async def test_getBlocksAtHeight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getBlocksAtHeight(classes.GetBlocksAtHeightParams(height=0, include_txs=False))
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getBlockByHash():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getBlockByHash(classes.GetBlockByHashParams(hash="6d51e50e6f864c844726f92e6d2d7d5d09f6e78921c1269f8796943eec7db98a", include_txs=False))
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getTopBlock():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getTopBlock(classes.GetTopBlockParams(include_txs=False))
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getNonce():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getNonce(address=TESTNET_ADDR)
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_hasNonce():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.hasNonce(address=TESTNET_ADDR)
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getNonceAtTopoheight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getNonceAtTopoheight(params=classes.GetNonceAtTopoheightParams(address=TESTNET_ADDR, topoheight=632))
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getBalance():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getBalance(params=classes.GetBalanceParams(address=TESTNET_ADDR, asset=XELIS_ASSET))
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_hasBalance():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.hasBalance(params=classes.GetBalanceParams(address=TESTNET_ADDR, asset=XELIS_ASSET))
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getBalanceAtTopoheight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getBalanceAtTopoheight(params=classes.GetBalanceAtTopoheightParams(address=TESTNET_ADDR, asset=XELIS_ASSET, topoheight=632))
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getAsset():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getAsset(asset=XELIS_ASSET)
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getAssets():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getAssets(params=classes.GetAssetsParams())
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_countAssets():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.countAssets()
  print(data)
  await daemon.close()  

@pytest.mark.asyncio
async def test_countTransactions():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.countTransactions()
  print(data)
  await daemon.close()
    
@pytest.mark.asyncio
async def test_countAccounts():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.countAccounts()
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getTips():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getTips()
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_p2pStatus():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.p2pStatus()
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getDAGorder():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getDAGOrder(params=classes.GetTopoheightRangeParams(start_topoheight=0, end_topoheight=1))
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getMempool():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getMempool()
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getTransaction():
  daemon = DaemonWS(url=MAINNET_NODE_WS)
  data = await daemon.getTransaction(hash="33b14221e79c0083e90141b22023d053d112f24ffc0d03d676291d19302ed03d")
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getTransactions():
  daemon = DaemonWS(url=MAINNET_NODE_WS)
  params = classes.GetTransactionsParams(tx_hashes=["33b14221e79c0083e90141b22023d053d112f24ffc0d03d676291d19302ed03d"])
  data = await daemon.getTransactions(params=params)
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getBlocksRangeByTopoheight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  params = classes.GetTopoheightRangeParams(start_topoheight=0, end_topoheight=10)
  data = await daemon.getBlocksRangeByTopoheight(params=params)
  print(data)
  await daemon.close()

@pytest.mark.asyncio
async def test_getBlocksRangeByHeight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  params = classes.GetHeightRangeParams(start_height=0, end_height=10)
  data = await daemon.getBlocksRangeByHeight(params=params)
  print(data)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getAcounts():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  params = classes.GetAssetsParams()
  result = await daemon.getAccounts(params=params)
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getAccountHistory():
  daemon = DaemonWS(url=MAINNET_NODE_WS)
  #dev fee wallet
  result = await daemon.getAccountHistory(address="xel:vs3mfyywt0fjys0rgslue7mm4wr23xdgejsjk0ld7f2kxng4d4nqqnkdufz")
  print(result)
  
  result = await daemon.getAccountHistory(address="xel:qcd39a5u8cscztamjuyr7hdj6hh2wh9nrmhp86ljx2sz6t99ndjqqm7wxj8")
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getAccountAssets():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  result = await daemon.getAccountAssets(address=TESTNET_ADDR)
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getPeers():
  daemon = DaemonWS(url=MAINNET_NODE_WS)
  result = await daemon.getPeers()
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getDevFeeThresholds():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  result = daemon.getDevFeeThresholds()
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getSizeOnDisk():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  result = await daemon.getSizeOnDisk()
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_isTxExecutedInBlock():
  params = classes.IsTxExecutedInBlockParams(
    block_hash="f61a3e037b4c8ae8aff2ace3a499a6f552ccd4ddaabd2e2067fec20c0da71d8c", 
    tx_hash="c743d8d822cd553672f8f534ed71277e8e50cfa37af9826a1ee1e922f059b019",
  )
  daemon = DaemonWS(url=MAINNET_NODE_WS)
  result = await daemon.isTxExecutedInBlock(params=params)
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getAccountRegistrationTopoheight():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  result = await daemon.getAccountRegistrationTopoheight(address=TESTNET_ADDR)
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_isAccountRegistered():
  params = classes.IsAccountRegisteredParams(address=TESTNET_ADDR, in_stable_height=True)
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  result = await daemon.isAccountRegistered(params=params)
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_getDifficulty():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  result = await daemon.getDifficulty()
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_validateAddress():
  params = classes.ValidateAddressParams(address=TESTNET_ADDR, allow_integrated=False)
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  result = await daemon.validateAddress(params=params)
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_extractKeyFromAddress():
  params = classes.ExtractKeyFromAddressParams(address=TESTNET_ADDR, tx_as_hex=True)
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  result = await daemon.extractKeyFromAddress(params)
  print(result)
  
  params = classes.ExtractKeyFromAddressParams(address=TESTNET_ADDR, tx_as_hex=False)
  result = await daemon.extractKeyFromAddress(params)
  print(result)
  await daemon.close()
  
@pytest.mark.asyncio
async def test_multi_fetch():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  data = await daemon.getInfo()
  print(data)
  data = await daemon.getVersion()
  print(data)
  await daemon.close()

@pytest.mark.asyncio
async def test_onNewBlock():
  daemon = await ConnectDaemonWS(url=MAINNET_NODE_WS)

  while True:
    block = await daemon.onNewBlock()
    if block is None:
      break
    else:
      print(block)
      await daemon.closeEvent(events.NewBlock)
      
  await daemon.close()
  
@pytest.mark.asyncio
async def test_listenToEvents():
  daemon = await ConnectDaemonWS(url=MAINNET_NODE_WS)
  
  async def onBlock():
    while True:
      data = await daemon.listenEvent("new_block")
      if data is None:
        break
      else:
        print(data)
      
  async def onBlockOrdered():
    while True:
      data = await daemon.listenEvent("block_ordered")
      if data is None:
        break
      else:
        print(data)
  
  async def closeEvents():
    await asyncio.sleep(30)
    await daemon.closeEvent("new_block")
    await daemon.closeEvent("block_ordered")
  
  await asyncio.gather(onBlock(), onBlockOrdered(), closeEvents())
  await daemon.close()
  
@pytest.mark.asyncio
async def test_gather_fetch():
  daemon = await ConnectDaemonWS(url=TESTNET_NODE_WS)
  
  info, version = await asyncio.gather(daemon.getInfo(), daemon.getVersion())
  print(info, version)
  await daemon.close()
