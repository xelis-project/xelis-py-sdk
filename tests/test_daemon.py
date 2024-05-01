from daemon.module import Daemon
from config.module import TESTNET_NODE_RPC

daemon = Daemon(TESTNET_NODE_RPC)

TESTNET_ADDR = "xet:rsdm79np9eqar7cg5jy9sdhwas74l4ml5enaasmae8jtjcvpr3vqqnlpysy"

def test_getInfo():
  data = daemon.getInfo()
  print(data)
  
def test_getVersion():
  version = daemon.getVersion()
  print(version)
  
def test_getBlockTemplate():
  result = daemon.getBlockTemplate(TESTNET_ADDR)
  print(result)