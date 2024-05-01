from config.module import TESTNET_NODE_WS
from daemon.websocket import DaemonWS

def test_getInfo():
  daemon = DaemonWS(url=TESTNET_NODE_WS)
  data = daemon.getInfo()
  print(data)
  daemon.close()