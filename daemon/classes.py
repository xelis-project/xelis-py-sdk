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