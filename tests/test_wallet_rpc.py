from config.module import LOCAL_WALLET_RPC
from wallet.http import WalletRPC

localWallet = WalletRPC(url=LOCAL_WALLET_RPC, username="test", password="test")

def test_GetVersion():
  data = localWallet.getVersion()
  print(data)