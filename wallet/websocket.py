from rpc.websocket import RPCWS
import wallet.methods as methods
from rpc.util import createBasicAuthToken

class WalletWS(RPCWS):
  def __init__(self, url: str, username: str, password: str) -> None:
    authToken = createBasicAuthToken(username=username, password=password)
    super().__init__(url, headers={ "Authorization": authToken })
  
  def getVersion(self):
    data = self.send(method=methods.GetVersion)
    return str(data)