DAEMON_RPC_PORT = "8080"
WALLET_RPC_PORT = "8081"
XSWD_PORT = "44325"

LOCAL_URL = "127.0.0.1"
TESTNET_NODE_URL = "testnet-node.xelis.io"
MAINNET_NODE_URL = "node.xelis.io"

LOCAL_NODE_RPC = "http://{}:{}/json_rpc".format(LOCAL_URL, DAEMON_RPC_PORT)
TESTNET_NODE_RPC = "https://{}/json_rpc".format(TESTNET_NODE_URL)
MAINNET_NODE_RPC = "https://{}/json_rpc".format(MAINNET_NODE_URL)

LOCAL_NODE_WS = "ws://{}:{}/json_rpc".format(LOCAL_URL, DAEMON_RPC_PORT)
TESTNET_NODE_WS = "wss://{}/json_rpc".format(TESTNET_NODE_URL)
MAINNET_NODE_URL = "wss://{}/json_rpc".format(MAINNET_NODE_URL)

LOCAL_WALLET_RPC = "http://{}:{}/json_rpc".format(LOCAL_URL, WALLET_RPC_PORT)
LOCAL_WALLET_WS = "ws://{}:{}/json_rpc".format(LOCAL_URL, WALLET_RPC_PORT)