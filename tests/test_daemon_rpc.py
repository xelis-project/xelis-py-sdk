from daemon.classes import GetBlockAtTopoheightParams
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
  
def test_getBlockTemplate():
  result = testnetDaemon.getBlockTemplate(address=TESTNET_ADDR)
  print(result)
  
def test_getBlockAtTopoheight():
  params = GetBlockAtTopoheightParams(topoheight=0, include_txs=False)
  result = testnetDaemon.getBlockAtTopoheight(params=params)
  print(result)