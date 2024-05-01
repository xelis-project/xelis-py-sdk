from websockets.sync.client import connect, ClientConnection
from rpc.websocket import RPCWS
import wallet.methods as methods
from rpc.util import createBasicAuthToken

class WalletWS(RPCWS):
  def __init__(self, client: ClientConnection = None, url: str = None, username: str = None, password: str = None) -> None:
    if url is not None:
      authToken = createBasicAuthToken(username=username, password=password)
      client = connect(uri=url, additional_headers={ "Authorization": authToken })

    super().__init__(client)
  
  def getVersion(self):
    data = self.send(method=methods.GetVersion)
    return str(data)