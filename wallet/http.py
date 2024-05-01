from rpc.http import RPCHttp
import wallet.methods as methods
from rpc.util import createBasicAuthToken

class WalletRPC(RPCHttp):
  authToken: str
  
  def __init__(self, url: str, username: str, password: str) -> None:
    self.authToken = createBasicAuthToken(username=username, password=password)
    super().__init__(url)
  
  def fetch(self, method: str, params=None):
    return super().fetch(method, params, { "Authorization": self.authToken })
  
  def getVersion(self):
    data = self.fetch(method=methods.GetVersion)
    return str(data)