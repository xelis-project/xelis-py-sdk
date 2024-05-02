import daemon.classes as classes
from daemon.http import DaemonRPC
from config.module import TESTNET_NODE_RPC, MAINNET_NODE_RPC, XELIS_ASSET

testnetDaemon = DaemonRPC(url=TESTNET_NODE_RPC)
mainnetDaemon = DaemonRPC(url=MAINNET_NODE_RPC)

TESTNET_ADDR = "xet:rsdm79np9eqar7cg5jy9sdhwas74l4ml5enaasmae8jtjcvpr3vqqnlpysy"

def test_noConnect():
  try:
    noDaemon = DaemonRPC(url="http://127.0.0.1:57432")
    data = noDaemon.getInfo()
  except Exception as err:
      print(err)

def test_getInfo():
  data = testnetDaemon.getInfo()
  print(data)
  
def test_getVersion():
  version = testnetDaemon.getVersion()
  print(version)
  
def test_getHeight():
  result = testnetDaemon.getHeight()
  print(result)
  
def test_getTopoheight():
  result = testnetDaemon.getTopoheight()
  print(result)
  
def test_getStableheight():
  result = testnetDaemon.getStableheight()
  print(result)
  
def test_getBlockTemplate():
  result = testnetDaemon.getBlockTemplate(address=TESTNET_ADDR)
  print(result)
  
def test_getBlockAtTopoheight():
  params = classes.GetBlockAtTopoheightParams(topoheight=0, include_txs=False)
  result = testnetDaemon.getBlockAtTopoheight(params=params)
  print(result)

def test_getBlocksAtHeight():
  params = classes.GetBlocksAtHeightParams(height=0, include_txs=False)
  result = testnetDaemon.getBlocksAtHeight(params=params)
  print(result)

def test_getBlockByHash():
  params = classes.GetBlockByHashParams(hash="6d51e50e6f864c844726f92e6d2d7d5d09f6e78921c1269f8796943eec7db98a", include_txs=False)
  result = testnetDaemon.getBlockByHash(params=params)
  print(result)
  
def test_getTopBlock():
  params = classes.GetTopBlockParams(include_txs=False)
  result = testnetDaemon.getTopBlock(params=params)
  print(result)
  
def test_getNonce():
  result = testnetDaemon.getNonce(address=TESTNET_ADDR)
  print(result)
  
def test_hasNonce():
  result = testnetDaemon.hasNonce(address=TESTNET_ADDR)
  print(result)
  
def test_getNonceAtTopoheight():
  params = classes.GetNonceAtTopoheightParams(address=TESTNET_ADDR, topoheight=632)
  result = testnetDaemon.getNonceAtTopoheight(params=params)
  print(result)
  
def test_getBalance():
  params = classes.GetBalanceParams(address=TESTNET_ADDR, asset=XELIS_ASSET)
  result = testnetDaemon.getBalance(params=params)
  print(result)
  
def test_hasBalance():
  params = classes.GetBalanceParams(address=TESTNET_ADDR, asset=XELIS_ASSET)
  result = testnetDaemon.hasBalance(params=params)
  print(result)
  
def test_getBalancecAtTopoheight():
  params = classes.GetBalanceAtTopoheightParams(address=TESTNET_ADDR, asset=XELIS_ASSET, topoheight=632)
  result = testnetDaemon.getBalanceAtTopoheight(params=params)
  print(result)
  
def test_getAsset():
  result = testnetDaemon.getAsset(asset=XELIS_ASSET)
  print(result)
  
def test_getAssets():
  params = classes.GetAssetsParams()
  result = testnetDaemon.getAssets(params=params)
  print(result)
  
def test_countAssets():
  result = testnetDaemon.countAssets()
  print(result)

def test_countTransactions():
  result = testnetDaemon.countTransactions()
  print(result)

def test_countAccounts():
  result = testnetDaemon.countAccounts()
  print(result)
  
def test_getTips():
  result = testnetDaemon.getTips()
  print(result)
  
def test_p2pStatus():
  result = testnetDaemon.p2pStatus()
  print(result)
  
def test_getDAGOrder():
  result = testnetDaemon.getDAGOrder(params=classes.GetTopoheightRangeParams(
    start_topoheight=0,
    end_topoheight=1
  ))
  print(result)
  
def test_getMempool():
  result = mainnetDaemon.getMempool()
  print(result)
  
def test_getTransaction():
  result = mainnetDaemon.getTransaction(hash="33b14221e79c0083e90141b22023d053d112f24ffc0d03d676291d19302ed03d")
  print(result)
  
def test_getTransactions():
  params = classes.GetTransactionsParams(tx_hashes=["33b14221e79c0083e90141b22023d053d112f24ffc0d03d676291d19302ed03d"])
  result = mainnetDaemon.getTransactions(params=params)
  print(result)
  
def test_getBlocksRangeByTopoheight():
  params = classes.GetTopoheightRangeParams(start_topoheight=0, end_topoheight=10)
  result = testnetDaemon.getBlocksRangeByTopoheight(params=params)
  print(result)
  
def test_getBlocksRangeByHeight():
  params = classes.GetHeightRangeParams(start_height=0, end_height=10)
  result = testnetDaemon.getBlocksRangeByHeight(params=params)
  print(result)
  
def test_getAcounts():
  params = classes.GetAssetsParams()
  result = testnetDaemon.getAccounts(params=params)
  print(result)
  
def test_getAccountHistory():
  #dev fee wallet
  result = mainnetDaemon.getAccountHistory(address="xel:vs3mfyywt0fjys0rgslue7mm4wr23xdgejsjk0ld7f2kxng4d4nqqnkdufz")
  print(result)
  
  result = mainnetDaemon.getAccountHistory(address="xel:qcd39a5u8cscztamjuyr7hdj6hh2wh9nrmhp86ljx2sz6t99ndjqqm7wxj8")
  print(result)
  
def test_getAccountAssets():
  result = testnetDaemon.getAccountAssets(address=TESTNET_ADDR)
  print(result)