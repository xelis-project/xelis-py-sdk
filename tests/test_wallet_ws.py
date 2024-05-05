import daemon
from wallet import classes
from wallet.websocket import WalletWS
from config.module import LOCAL_WALLET_WS, XELIS_ASSET

username = "test"
password = "test"

def test_getVersion():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = wallet.getVersion()
  print(data)
  wallet.close()
  
def test_getNetwork():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = wallet.getNetwork()
  print(data)
  wallet.close()
  
def test_getNonce():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = wallet.getNonce()
  print(data)
  wallet.close()
  
def test_getTopoheight():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = wallet.getTopoheight()
  print(data)
  wallet.close()
  
def test_getAddress():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetAddressParams()
  data = wallet.getAddress(params=params)
  print(data)
  wallet.close()
  
def test_splitAddress():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetAddressParams(integrated_data={ "hello": "world" })
  integratedAddr = wallet.getAddress(params=params)
  print(integratedAddr)

  params = classes.SplitAddressParams(address=integratedAddr)
  data = wallet.splitAddress(params=params)
  print(data)
  wallet.close()

def test_rescan():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.RescanParams(until_topoheight=0)
  data = wallet.rescan(params=params)
  print(data)
  wallet.close()

def test_getBalance():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetBalanceParams(asset=XELIS_ASSET)
  data = wallet.getBalance(params=params)
  print(data)
  wallet.close()
  
def test_hasBalance():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetBalanceParams(asset=XELIS_ASSET)
  data = wallet.hasBalance(params=params)
  print(data)
  wallet.close()
  
def test_getTrackedAssets():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = wallet.getTrackedAssets()
  print(data)
  wallet.close()
  
def test_getAssetPrecision():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetBalanceParams(asset=XELIS_ASSET)
  data = wallet.getAssetPrecision(params=params)
  print(data)
  wallet.close()
  
def test_getTransaction():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = wallet.getTransaction(hash="ca03ed1b552d0f7327638996e1024e3fec0d6bd328ccc42299e6d699c9d8233d")
  print(data)
  wallet.close()
  
def test_buildTransaction():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.BuildTransactionParams(
    broadcast=False,
    tx_as_hex=True,
    #transfers=[],
    burn=daemon.classes.Burn(asset=XELIS_ASSET, amount=0)
  )
  data = wallet.buildTransaction(params=params)
  print(data)
  wallet.close()
  
def test_listTransactions():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.ListTransactionsParams()
  data = wallet.listTransactions(params=params)
  print(data)
  wallet.close()
  
def test_isOnline():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = wallet.isOnline()
  print(data)
  wallet.close()
  
def test_setOnlineMode():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.SetOnlineModeParams(daemon_address="127.0.0.1:8080")
  data = wallet.setOnlineMode(params=params)
  print(data)
  wallet.close()
  
def test_setOfflineMode():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = wallet.setOfflineMode()
  print(data)
  wallet.close()
  
def test_signData():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = wallet.signData("hello world")
  print(data)
  wallet.close()
  
def test_estimateFees():
  wallet = WalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.EstimateFeesParams(
    transfers=[],
    #burn=daemon.classes.Burn(asset=XELIS_ASSET, amount=0)
  )
  data = wallet.estimateFees(params=params)
  print(data)
  wallet.close()