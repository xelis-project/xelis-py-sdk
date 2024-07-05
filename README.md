# XELIS-PY-SDK

Xelis software development kit for Python.

## Install

Install library with PIP.

`pip install xelis-py-sdk`

## Usage

```python
from xelis.daemon.http import DaemonRPC
from xelis.config.module import MAINNET_NODE_RPC

mainnetDaemon = DaemonRPC(url=MAINNET_NODE_RPC)
data = mainnetDaemon.getInfo()
```

Check test files for more examples ex: `tests/test_daemon_rpc.py`.
