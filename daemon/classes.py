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
