from requests import post
from dacite import from_dict

from daemon.classes import GetBlockTemplateResult, GetInfoResult

class Daemon:
  def __init__(self, url: str) -> None:
    self.url = url

  def fetch(self, method: str, params: dict[str, any] = None):
    data = {
      "id": 1,
      "jsonrpc": "2.0",
      "method": method
    }
    print(data)
    if params is not None:
      data["params"] = params

    headers = { "Content-Type": "application/json" }

    res = post(self.url, json=data, headers=headers)
    data = res.json()
    if "error" in data:
      raise ValueError(data["error"]["message"])
    
    return data["result"]

  def getInfo(self) -> GetInfoResult:
    data = self.fetch(method="get_info")
    return from_dict(data_class=GetInfoResult, data=data)
  
  def getVersion(self) -> str:
    data = self.fetch(method="get_version")
    return str(data)
  
  def getHeight(self) -> int:
    data = self.fetch(method="get_height")
    return int(data)
  
  def getTopoheight(self) -> int:
    data = self.fetch(method="get_topoheight")
    return int(data)
  
  def getStableheight(self) -> int:
    data = self.fetch(method="get_stableheight")
    return int(data)
  
  def getBlockTemplate(self, address: str):
    data = self.fetch(method="get_block_template", params={ "address": address })
    return from_dict(data_class=GetBlockTemplateResult, data=data)