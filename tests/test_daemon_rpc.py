import xelis.daemon.classes as daemonClasses
from xelis.daemon.http import DaemonRPC
from xelis.config.module import LOCAL_NODE_RPC, TESTNET_NODE_RPC, MAINNET_NODE_RPC, XELIS_ASSET

testnetDaemon = DaemonRPC(url=TESTNET_NODE_RPC)
mainnetDaemon = DaemonRPC(url=MAINNET_NODE_RPC)
localDaemon = DaemonRPC(url=LOCAL_NODE_RPC)

TESTNET_ADDR = "xet:62wnkswt0rmrdd9d2lawgpzuh87fkpmp4gx9j3g4u24yrdkdxgksqnuuucf"

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
  
def test_getStableHeight():
  result = testnetDaemon.getStableHeight()
  print(result)
  
def test_getBlockTemplate():
  result = testnetDaemon.getBlockTemplate(address=TESTNET_ADDR)
  print(result)
  
def test_getBlockAtTopoheight():
  params = daemonClasses.GetBlockAtTopoheightParams(topoheight=0, include_txs=False)
  result = testnetDaemon.getBlockAtTopoheight(params=params)
  print(result)

def test_getBlocksAtHeight():
  params = daemonClasses.GetBlocksAtHeightParams(height=0, include_txs=False)
  result = testnetDaemon.getBlocksAtHeight(params=params)
  print(result)

def test_getBlockByHash():
  params = daemonClasses.GetBlockByHashParams(hash="b0086a1d89215d306ac5e48ae9333c8b91ea7d4263851df1deb42b04a30549bf", include_txs=False)
  result = testnetDaemon.getBlockByHash(params=params)
  print(result)
  
def test_getTopBlock():
  params = daemonClasses.GetTopBlockParams(include_txs=False)
  result = testnetDaemon.getTopBlock(params=params)
  print(result)
  
def test_getNonce():
  result = testnetDaemon.getNonce(address=TESTNET_ADDR)
  print(result)
  
def test_hasNonce():
  result = testnetDaemon.hasNonce(address=TESTNET_ADDR)
  print(result)
  
def test_getNonceAtTopoheight():
  params = daemonClasses.GetNonceAtTopoheightParams(address=TESTNET_ADDR, topoheight=38665)
  result = testnetDaemon.getNonceAtTopoheight(params=params)
  print(result)
  
def test_getBalance():
  params = daemonClasses.GetBalanceParams(address=TESTNET_ADDR, asset=XELIS_ASSET)
  result = testnetDaemon.getBalance(params=params)
  print(result)
  
def test_getStableBalance():
  params = daemonClasses.GetBalanceParams(address=TESTNET_ADDR, asset=XELIS_ASSET)
  result = testnetDaemon.getStableBalance(params=params)
  print(result)
  
def test_hasBalance():
  params = daemonClasses.GetBalanceParams(address=TESTNET_ADDR, asset=XELIS_ASSET)
  result = testnetDaemon.hasBalance(params=params)
  print(result)
  
def test_getBalancecAtTopoheight():
  params = daemonClasses.GetBalanceAtTopoheightParams(address=TESTNET_ADDR, asset=XELIS_ASSET, topoheight=38665)
  result = testnetDaemon.getBalanceAtTopoheight(params=params)
  print(result)
  
def test_getAsset():
  result = testnetDaemon.getAsset(asset=XELIS_ASSET)
  print(result)
  
def test_getAssets():
  params = daemonClasses.GetAssetsParams()
  result = testnetDaemon.getAssets(params=params)
  print(result)
  
def test_countAssets():
  result = testnetDaemon.countAssets()
  print(result)

def test_countTransactions():
  result = testnetDaemon.countTransactions()
  print(result)

def test_countAccounts():
  result = testnetDaemon.countAccounts()
  print(result)
  
def test_getTips():
  result = testnetDaemon.getTips()
  print(result)
  
def test_p2pStatus():
  result = testnetDaemon.p2pStatus()
  print(result)
  
def test_getDAGOrder():
  result = testnetDaemon.getDAGOrder(params=daemonClasses.GetTopoheightRangeParams(
    start_topoheight=0,
    end_topoheight=1
  ))
  print(result)
  
def test_getMempool():
  result = mainnetDaemon.getMempool()
  print(result)
  
def test_getTransaction():
  result = mainnetDaemon.getTransaction(hash="33b14221e79c0083e90141b22023d053d112f24ffc0d03d676291d19302ed03d")
  print(result)

def test_checkExtraData():
  # v2
  result = localDaemon.getTransaction(hash="389426d5f181f2b7e503052bd19bccbad344262ad8d90c39a87aa6d5dbd86669")
  size = len(result.data.transfers[0].extra_data)
  print(size)

  # v1
  result = localDaemon.getTransaction(hash="6d2478c646e629cd944afd0d6232d359e4b652c3b0104cc15c7af2bba90c8fce")
  size = len(result.data.transfers[0].extra_data)
  print(size)
  
  # v1
  result = localDaemon.getTransaction(hash="067f2b8876cf4bf1e96318f0706bb121116d2138b0396c9dc16319ff315648e7")
  size = len(result.data.transfers[0].extra_data)
  print(size)
  
  # v2
  result = localDaemon.getTransaction(hash="009247c48a4e4a03f4c69dadaf1279103ed1d7ff2b2c3d98c3a7b2911d8d69fd")
  size = len(result.data.transfers[0].extra_data)
  print(size)

def test_getTransactions():
  params = daemonClasses.GetTransactionsParams(tx_hashes=["33b14221e79c0083e90141b22023d053d112f24ffc0d03d676291d19302ed03d"])
  result = mainnetDaemon.getTransactions(params=params)
  print(result)
  
def test_getBlocksRangeByTopoheight():
  params = daemonClasses.GetTopoheightRangeParams(start_topoheight=0, end_topoheight=10)
  result = testnetDaemon.getBlocksRangeByTopoheight(params=params)
  print(result)
  
def test_getBlocksRangeByHeight():
  params = daemonClasses.GetHeightRangeParams(start_height=0, end_height=10)
  result = testnetDaemon.getBlocksRangeByHeight(params=params)
  print(result)
  
def test_getAcounts():
  params = daemonClasses.GetAssetsParams()
  result = testnetDaemon.getAccounts(params=params)
  print(result)
  
def test_getAccountHistory():
  #dev fee wallet
  result = mainnetDaemon.getAccountHistory(address="xel:vs3mfyywt0fjys0rgslue7mm4wr23xdgejsjk0ld7f2kxng4d4nqqnkdufz")
  print(result)
  
  result = mainnetDaemon.getAccountHistory(address="xel:qcd39a5u8cscztamjuyr7hdj6hh2wh9nrmhp86ljx2sz6t99ndjqqm7wxj8")
  print(result)
  
def test_getAccountAssets():
  result = testnetDaemon.getAccountAssets(address=TESTNET_ADDR)
  print(result)
  
def test_getPeers():
  result = testnetDaemon.getPeers()
  print(result)
  
def test_getDevFeeThresholds():
  result = testnetDaemon.getDevFeeThresholds()
  print(result)
  
def test_getSizeOnDisk():
  result = testnetDaemon.getSizeOnDisk()
  print(result)
  
def test_isTxExecutedInBlock():
  params = daemonClasses.IsTxExecutedInBlockParams(
    block_hash="f61a3e037b4c8ae8aff2ace3a499a6f552ccd4ddaabd2e2067fec20c0da71d8c", 
    tx_hash="c743d8d822cd553672f8f534ed71277e8e50cfa37af9826a1ee1e922f059b019",
  )
  result = mainnetDaemon.isTxExecutedInBlock(params=params)
  print(result)
  
def test_getAccountRegistrationTopoheight():
  result = testnetDaemon.getAccountRegistrationTopoheight(address=TESTNET_ADDR)
  print(result)
  
def test_isAccountRegistered():
  params = daemonClasses.IsAccountRegisteredParams(address=TESTNET_ADDR, in_stable_height=True)
  result = testnetDaemon.isAccountRegistered(params=params)
  print(result)

def test_getDifficulty():
  result = testnetDaemon.getDifficulty()
  print(result)
  
def test_validateAddress():
  params = daemonClasses.ValidateAddressParams(address=TESTNET_ADDR, allow_integrated=False)
  result = testnetDaemon.validateAddress(params=params)
  print(result)
  
def test_extractKeyFromAddress():
  params = daemonClasses.ExtractKeyFromAddressParams(address=TESTNET_ADDR, as_hex=True)
  result = testnetDaemon.extractKeyFromAddress(params)
  print(result)
  
  params = daemonClasses.ExtractKeyFromAddressParams(address=TESTNET_ADDR, as_hex=False)
  result = testnetDaemon.extractKeyFromAddress(params)
  print(result)
  