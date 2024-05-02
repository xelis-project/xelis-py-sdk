from dataclasses import dataclass, field

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
class GetHeightRangeParams:
  start_height: int
  end_height: int

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

@dataclass
class SubmitBlockParams:
  block_template: str
  miner_work: str = None

@dataclass
class Proof:
  Y_0: list[int]
  Y_1: list[int]
  z_r: list[int]
  z_x: list[int]

@dataclass
class Burn:
  asset: str
  amount: int

@dataclass
class Transfer:
  asset: str
  extra_data: list[int] | None
  destination: str
  commitment: list[int]
  sender_handle: list[int]
  receiver_handle: list[int]
  ct_validity_proof: Proof

@dataclass
class EqProof:
  Y_0: list[int]
  Y_1: list[int]
  Y_2: list[int]
  z_r: list[int]
  z_s: list[int]
  z_x: list[int]

@dataclass
class SourceCommitment:
  commitment: list[int]
  proof: EqProof
  asset: str
  
@dataclass
class Reference:
  hash: str
  topoheight: int
  
@dataclass
class TransactionData:
  transfers: list[Transfer]
  burn: Burn | None

@dataclass
class Transaction:
  blocks: list[str] | None
  hash: str
  data: TransactionData
  fee: int
  nonce: int
  source: str
  reference: Reference
  source_commitments: list[SourceCommitment]
  range_proof: list[int]
  signature: str
  executed_in_block: str | None
  version: int
  first_seen: int | None
  in_mempool: bool
  
@dataclass
class GetTransactionsParams:
  tx_hashes: list[str]

@dataclass
class MiningHistory:
  reward: int
  
@dataclass
class BurnHistory:
  amount: int
  
@dataclass
class OutgoingHistory:
  to: str
  
@dataclass()
class IncomingHistory:
  from_: str

@dataclass
class DevFeeHistory:
  reward: int

@dataclass
class AccountHistory:
  topoheight: int
  block_timestamp: int
  hash: str
  mining: MiningHistory | None
  burn: BurnHistory | None
  outgoing: OutgoingHistory | None
  incoming: IncomingHistory | None
  dev_fee: MiningHistory | None