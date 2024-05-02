from config.module import TESTNET_NODE_WS, XELIS_ASSET
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