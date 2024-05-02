from config.module import TESTNET_NODE_WS, XELIS_ASSET, MAINNET_NODE_WS
from daemon.websocket import DaemonWS
import daemon.classes as classes

TESTNET_ADDR = "xet:rsdm79np9eqar7cg5jy9sdhwas74l4ml5enaasmae8jtjcvpr3vqqnlpysy"

def test_daemon():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getInfo()
  print(data)
  daemon.close()
  
def test_getVersion():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getVersion()
  print(data)
  daemon.close()
    
def test_getHeight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getHeight()
  print(data)
  daemon.close()
    
def test_getTopoheight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getTopoheight()
  print(data)
  daemon.close()
    
def test_getStableheight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getStableheight()
  print(data)
  daemon.close()
    
def test_getBlockTemplate():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getBlockTemplate(address=TESTNET_ADDR)
  print(data)
  daemon.close()
    
def test_getBlockAtTopoheight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getBlockAtTopoheight(classes.GetBlockAtTopoheightParams(topoheight=0, include_txs=False))
  print(data)
  daemon.close()
    
def test_getBlocksAtHeight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getBlocksAtHeight(classes.GetBlocksAtHeightParams(height=0, include_txs=False))
  print(data)
  daemon.close()
  
def test_getBlockByHash():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getBlockByHash(classes.GetBlockByHashParams(hash="6d51e50e6f864c844726f92e6d2d7d5d09f6e78921c1269f8796943eec7db98a", include_txs=False))
  print(data)
  daemon.close()
  
def test_getTopBlock():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getTopBlock(classes.GetTopBlockParams(include_txs=False))
  print(data)
  daemon.close()
  
def test_getNonce():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getNonce(address=TESTNET_ADDR)
  print(data)
  daemon.close()
  
def test_hasNonce():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.hasNonce(address=TESTNET_ADDR)
  print(data)
  daemon.close()
  
def test_getNonceAtTopoheight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getNonceAtTopoheight(params=classes.GetNonceAtTopoheightParams(address=TESTNET_ADDR, topoheight=632))
  print(data)
  daemon.close()
  
def test_getBalance():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getBalance(params=classes.GetBalanceParams(address=TESTNET_ADDR, asset=XELIS_ASSET))
  print(data)
  daemon.close()
  
def test_hasBalance():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.hasBalance(params=classes.GetBalanceParams(address=TESTNET_ADDR, asset=XELIS_ASSET))
  print(data)
  daemon.close()
  
def test_getBalanceAtTopoheight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getBalanceAtTopoheight(params=classes.GetBalanceAtTopoheightParams(address=TESTNET_ADDR, asset=XELIS_ASSET, topoheight=632))
  print(data)
  daemon.close()
  
def test_getAsset():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getAsset(asset=XELIS_ASSET)
  print(data)
  daemon.close()
  
def test_getAssets():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getAssets(params=classes.GetAssetsParams())
  print(data)
  daemon.close()
  
def test_countAssets():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.countAssets()
  print(data)
  daemon.close()  

def test_countTransactions():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.countTransactions()
  print(data)
  daemon.close()
    
def test_countAccounts():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.countAccounts()
  print(data)
  daemon.close()
  
def test_getTips():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getTips()
  print(data)
  daemon.close()
  
def test_p2pStatus():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.p2pStatus()
  print(data)
  daemon.close()
  
def test_getDAGorder():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getDAGOrder(params=classes.GetTopoheightRangeParams(start_topoheight=0, end_topoheight=1))
  print(data)
  daemon.close()
  
def test_getMempool():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getMempool()
  print(data)
  daemon.close()
  
def test_getTransaction():
  daemon = DaemonWS(url=MAINNET_NODE_WS)
  data = daemon.getTransaction(hash="33b14221e79c0083e90141b22023d053d112f24ffc0d03d676291d19302ed03d")
  print(data)
  daemon.close()
  
def test_getTransactions():
  daemon = DaemonWS(url=MAINNET_NODE_WS)
  params = classes.GetTransactionsParams(tx_hashes=["33b14221e79c0083e90141b22023d053d112f24ffc0d03d676291d19302ed03d"])
  data = daemon.getTransactions(params=params)
  print(data)
  daemon.close()
  
def test_getBlocksRangeByTopoheight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  params = classes.GetTopoheightRangeParams(start_topoheight=0, end_topoheight=10)
  data = daemon.getBlocksRangeByTopoheight(params=params)
  print(data)
  daemon.close()

def test_getBlocksRangeByHeight():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  params = classes.GetHeightRangeParams(start_height=0, end_height=10)
  data = daemon.getBlocksRangeByHeight(params=params)
  print(data)
  daemon.close()
  
def test_getAcounts():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  params = classes.GetAssetsParams()
  result = daemon.getAccounts(params=params)
  print(result)
  daemon.close()
  
def test_getAccountHistory():
  daemon = DaemonWS(url=MAINNET_NODE_WS)
  #dev fee wallet
  result = daemon.getAccountHistory(address="xel:vs3mfyywt0fjys0rgslue7mm4wr23xdgejsjk0ld7f2kxng4d4nqqnkdufz")
  print(result)
  
  result = daemon.getAccountHistory(address="xel:qcd39a5u8cscztamjuyr7hdj6hh2wh9nrmhp86ljx2sz6t99ndjqqm7wxj8")
  print(result)
  daemon.close()
  
def test_getAccountAssets():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  result = daemon.getAccountAssets(address=TESTNET_ADDR)
  print(result)
  daemon.close()