from websockets.sync.client import connect, ClientConnection
from daemon.websocket import DaemonWS
from wallet.websocket import WalletWS
import xswd.classes as classes
import json

class XSWD():
  daemon: DaemonWS
  wallet: WalletWS
  client: ClientConnection
  
  def __init__(self, url: str) -> None:
    self.client = connect(uri=url)
    self.daemon = DaemonWS(client=self.client)
    self.daemon.prefix = "node."
    self.wallet = WalletWS(client=self.client)
    self.wallet.prefix = "wallet."

  def authorize(self, app: classes.ApplicationData):
    sendData = json.dumps(vars(app))
    self.client.send(sendData)
    recvData = self.client.recv()
    data = json.loads(recvData)
    if "error" in data:
      raise ValueError(data["error"]["message"])