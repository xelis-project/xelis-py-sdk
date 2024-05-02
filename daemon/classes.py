from dataclasses import dataclass

@dataclass
class GetInfoResult:
  average_block_time: int
  block_reward: int
  block_time_target: int
  circulating_supply: int
  difficulty: str
  height: int
  maximum_supply: int
  mempool_size: int
  network: str
  pruned_topoheight: int | None
  stableheight: int
  top_block_hash: str
  topoheight: int
  version: str
  
@dataclass
class GetBlockTemplateResult:
  template: str
  height: int
  topoheight: int
  difficulty: str
  
@dataclass
class GetBlockAtTopoheightParams:
  topoheight: int
  include_txs: bool
  
@dataclass
class GetBlocksAtHeightParams:
  height: int
  include_txs: bool
  
@dataclass
class GetBlockByHashParams:
  hash: str
  include_txs: bool
  
@dataclass
class GetTopBlockParams:
  include_txs: bool
  
@dataclass
class GetNonceResult:
  nonce: int
  previous_topoheight: int | None
  topoheight: int
  
@dataclass
class VersionedNonce:
  nonce: int
  previous_topoheight: int | None
  
@dataclass
class GetNonceAtTopoheightParams:
  address: str
  topoheight: int
  
@dataclass
class GetBalanceParams:
  address: str
  asset: str
  
@dataclass
class GetBalanceAtTopoheightParams:
  address: str
  asset: str
  topoheight: int

@dataclass
class EncryptedBalance:
  commitment: list[int]
  handle: list[int]
  
@dataclass
class VersionedBalance:
  balance_type: str # input, output or both
  final_balance: EncryptedBalance
  output_balance: EncryptedBalance | None
  previous_topoheight: int | None

@dataclass
class GetBalanceResult:
  version: VersionedBalance
  topoheight: int

@dataclass
class GetAssetsParams:
  Skip: int = None
  Maximum: int = None
  MinimumTopoheight: int = None
  MaximumTopoheight: int = None

@dataclass
class Asset:
  topoheight: int
  decimals: int

@dataclass
class AssetWithData:
  asset: str
  topoheight: int
  decimals: int
  
@dataclass
class P2PStatusResult:
  best_topoheight: int
  max_peers: int
  our_topoheight: int
  peer_count: int
  peer_id: int
  tag: str | None
  
@dataclass
class GetTopoheightRangeParams:
  start_topoheight: int
  end_topoheight: int

@dataclass
class Block:
  block_type: str
  cumulative_difficulty: str
  difficulty: str
  extra_nonce: str
  hash: str
  height: int
  miner: str
  nonce: int
  reward: int
  supply: int
  timestamp: int
  tips: list[str]
  topoheight: int
  total_fees: int | None
  total_size_in_bytes: int
  txs_hashes: list[str]
  version: int
