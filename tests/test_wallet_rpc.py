from config.module import LOCAL_WALLET_RPC, XELIS_ASSET
from wallet import classes
import daemon.classes
from wallet.http import WalletRPC

localWallet = WalletRPC(url=LOCAL_WALLET_RPC, username="test", password="test")

def test_GetVersion():
  data = localWallet.getVersion()
  print(data)
  
def test_getNetwork():
  data = localWallet.getNetwork()
  print(data)
  
def test_getNonce():
  data = localWallet.getNonce()
  print(data)
  
def test_getTopoheight():
  data = localWallet.getTopoheight()
  print(data)
  
def test_getAddress():
  params = classes.GetAddressParams()
  data = localWallet.getAddress(params=params)
  print(data)
  
def test_splitAddress():
  params = classes.GetAddressParams(integrated_data={ "hello": "world" })
  integratedAddr = localWallet.getAddress(params=params)
  print(integratedAddr)

  params = classes.SplitAddressParams(address=integratedAddr)
  data = localWallet.splitAddress(params=params)
  print(data)

def test_rescan():
  params = classes.RescanParams(until_topoheight=0)
  data = localWallet.rescan(params=params)
  print(data)

def test_getBalance():
  params = classes.GetBalanceParams(asset=XELIS_ASSET)
  data = localWallet.getBalance(params=params)
  print(data)
  
def test_hasBalance():
  params = classes.GetBalanceParams(asset=XELIS_ASSET)
  data = localWallet.hasBalance(params=params)
  print(data)
  
def test_getTrackedAssets():
  data = localWallet.getTrackedAssets()
  print(data)
  
def test_getAssetPrecision():
  params = classes.GetBalanceParams(asset=XELIS_ASSET)
  data = localWallet.getAssetPrecision(params=params)
  print(data)
  
def test_getTransaction():
  data = localWallet.getTransaction(hash="ca03ed1b552d0f7327638996e1024e3fec0d6bd328ccc42299e6d699c9d8233d")
  print(data)
  
def test_buildTransaction():
  params = classes.BuildTransactionParams(
    broadcast=False,
    tx_as_hex=True,
    #transfers=[],
    burn=daemon.classes.Burn(asset=XELIS_ASSET, amount=0)
  )
  data = localWallet.buildTransaction(params=params)
  print(data)
  
def test_listTransactions():
  params = classes.ListTransactionsParams()
  data = localWallet.listTransactions(params=params)
  print(data)
  
def test_isOnline():
  data = localWallet.isOnline()
  print(data)
  
def test_setOnlineMode():
  params = classes.SetOnlineModeParams(daemon_address="127.0.0.1:8080")
  data = localWallet.setOnlineMode(params=params)
  print(data)
  
def test_setOfflineMode():
  data = localWallet.setOfflineMode()
  print(data)
  
def test_signData():
  data = localWallet.signData("hello world")
  print(data)
  
def test_estimateFees():
  params = classes.EstimateFeesParams(
    transfers=[],
    #burn=daemon.classes.Burn(asset=XELIS_ASSET, amount=0)
  )
  data = localWallet.estimateFees(params=params)
  print(data)
  
def test_integratedAddr():
  params = classes.GetAddressParams(
    integrated_data="v3"
  )
  
  addr = localWallet.getAddress(params=params)
  print(addr)