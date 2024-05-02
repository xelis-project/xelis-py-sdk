import daemon.classes as classes
from daemon.http import DaemonRPC
from config.module import TESTNET_NODE_RPC, MAINNET_NODE_RPC

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