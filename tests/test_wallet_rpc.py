from xelis.daemon import classes as daemonClasses
from xelis.config.module import LOCAL_WALLET_RPC, XELIS_ASSET
from xelis.wallet import classes as walletClasses
from xelis.wallet.http import WalletRPC

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
  params = walletClasses.GetAddressParams()
  data = localWallet.getAddress(params=params)
  print(data)
  
def test_splitAddress():
  params = walletClasses.GetAddressParams(integrated_data={ "hello": "world" })
  integratedAddr = localWallet.getAddress(params=params)
  print(integratedAddr)

  params = walletClasses.SplitAddressParams(address=integratedAddr)
  data = localWallet.splitAddress(params=params)
  print(data)

def test_rescan():
  params = walletClasses.RescanParams(until_topoheight=0)
  data = localWallet.rescan(params=params)
  print(data)

def test_getBalance():
  params = walletClasses.GetBalanceParams(asset=XELIS_ASSET)
  data = localWallet.getBalance(params=params)
  print(data)
  
def test_hasBalance():
  params = walletClasses.GetBalanceParams(asset=XELIS_ASSET)
  data = localWallet.hasBalance(params=params)
  print(data)
  
def test_getTrackedAssets():
  data = localWallet.getTrackedAssets()
  print(data)
  
def test_getAssetPrecision():
  params = walletClasses.GetBalanceParams(asset=XELIS_ASSET)
  data = localWallet.getAssetPrecision(params=params)
  print(data)
  
def test_getTransaction():
  data = localWallet.getTransaction(hash="ca03ed1b552d0f7327638996e1024e3fec0d6bd328ccc42299e6d699c9d8233d")
  print(data)
  
def test_buildTransaction():
  params = walletClasses.BuildTransactionParams(
    broadcast=False,
    tx_as_hex=True,
    #transfers=[],
    burn=daemonClasses.Burn(asset=XELIS_ASSET, amount=0)
  )
  data = localWallet.buildTransaction(params=params)
  print(data)
  
def test_listTransactions():
  params = walletClasses.ListTransactionsParams()
  data = localWallet.listTransactions(params=params)
  print(data)
  
def test_isOnline():
  data = localWallet.isOnline()
  print(data)
  
def test_setOnlineMode():
  params = walletClasses.SetOnlineModeParams(daemon_address="127.0.0.1:8080")
  data = localWallet.setOnlineMode(params=params)
  print(data)
  
def test_setOfflineMode():
  data = localWallet.setOfflineMode()
  print(data)
  
def test_signData():
  data = localWallet.signData("hello world")
  print(data)
  
def test_estimateFees():
  params = walletClasses.EstimateFeesParams(
    transfers=[],
    #burn=daemon.classes.Burn(asset=XELIS_ASSET, amount=0)
  )
  data = localWallet.estimateFees(params=params)
  print(data)
  
def test_integratedAddr():
  params = walletClasses.GetAddressParams(
    integrated_data="v3"
  )
  
  addr = localWallet.getAddress(params=params)
  print(addr)