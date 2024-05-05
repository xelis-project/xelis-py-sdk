from config.module import LOCAL_XSWD_WS
from xswd.classes import ApplicationData
from xswd.module import XSWD

def test_xswd():
  xswd = XSWD(LOCAL_XSWD_WS)
  
  app = ApplicationData(
    id="9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08",
    name="Test App",
    description="This is a test app.",
  )
  
  xswd.authorize(app=app)

  info = xswd.daemon.getInfo()
  print(info)
  
  version = xswd.wallet.getVersion()
  print(version)