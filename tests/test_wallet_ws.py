from wallet.websocket import WalletWS
from config.module import LOCAL_WALLET_WS

def test_getVersion():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username="test", password="test")
  data = wallet.getVersion()
  print(data)
  wallet.close()