import pytest
from xelis.wallet import classes, events
from xelis.wallet.websocket import ConnectWalletWS
from xelis.config.module import LOCAL_WALLET_WS, XELIS_ASSET

username = "test"
password = "test"

@pytest.mark.asyncio
async def test_getVersion():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = await wallet.getVersion()
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_getNetwork():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = await wallet.getNetwork()
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_getNonce():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = await wallet.getNonce()
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_getTopoheight():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = await wallet.getTopoheight()
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_getAddress():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetAddressParams()
  data = await wallet.getAddress(params=params)
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_splitAddress():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetAddressParams(integrated_data={ "hello": "world" })
  integratedAddr = await wallet.getAddress(params=params)
  print(integratedAddr)

  params = classes.SplitAddressParams(address=integratedAddr)
  data = await wallet.splitAddress(params=params)
  print(data)
  await wallet.close()

@pytest.mark.asyncio
async def test_rescan():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.RescanParams(until_topoheight=0)
  data = await wallet.rescan(params=params)
  print(data)
  await wallet.close()

@pytest.mark.asyncio
async def test_getBalance():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetBalanceParams(asset=XELIS_ASSET)
  data = await wallet.getBalance(params=params)
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_hasBalance():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetBalanceParams(asset=XELIS_ASSET)
  data = await wallet.hasBalance(params=params)
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_getTrackedAssets():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = await wallet.getTrackedAssets()
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_getAssetPrecision():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.GetBalanceParams(asset=XELIS_ASSET)
  data = await wallet.getAssetPrecision(params=params)
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_getTransaction():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = await wallet.getTransaction(hash="ca03ed1b552d0f7327638996e1024e3fec0d6bd328ccc42299e6d699c9d8233d")
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_buildTransaction():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.BuildTransactionParams(
    broadcast=False,
    tx_as_hex=True,
    #transfers=[],
    burn=daemon.classes.Burn(asset=XELIS_ASSET, amount=0)
  )
  data = await wallet.buildTransaction(params=params)
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_listTransactions():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.ListTransactionsParams()
  data = await wallet.listTransactions(params=params)
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_isOnline():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = await wallet.isOnline()
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_setOnlineMode():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.SetOnlineModeParams(daemon_address="127.0.0.1:8080")
  data = await wallet.setOnlineMode(params=params)
  print(data)
  await wallet.close()

'''
@pytest.mark.asyncio
async def test_setOfflineMode():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = await wallet.setOfflineMode()
  print(data)
  await wallet.close()
'''
  
@pytest.mark.asyncio
async def test_signData():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  data = await wallet.signData("hello world")
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_estimateFees():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)
  params = classes.EstimateFeesParams(
    transfers=[],
    #burn=daemon.classes.Burn(asset=XELIS_ASSET, amount=0)
  )
  data = await wallet.estimateFees(params=params)
  print(data)
  await wallet.close()
  
@pytest.mark.asyncio
async def test_onNewTopoheight():
  wallet = await ConnectWalletWS(url=LOCAL_WALLET_WS, username=username, password=password)

  while True:
    topo = await wallet.onNewTopoheight()
    if topo is None:
      break
    else:
      print(topo)
      await wallet.closeEvent(events.NewTopoHeight)
      
  await wallet.close()