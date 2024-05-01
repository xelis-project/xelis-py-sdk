from requests import post
import base64

class RPCHttp:
  url: str
  
  def __init__(self, url: str) -> None:
    self.url = url

  def fetch(self, method: str, params = None, headers = {}):
    data = {
      "id": 1,
      "jsonrpc": "2.0",
      "method": method
    }

    if params is not None:
      data["params"] = params
      
    headers["Content-Type"] = "application/json"

    res = post(self.url, json=data, headers=headers)
    if res.ok:
      data = res.json()
      if "error" in data:
        raise ValueError(data["error"]["message"])
    
      return data["result"]
    
    raise Exception("POST request failed with status code {}: {}".format(res.status_code, res.text))