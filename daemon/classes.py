from dataclasses import dataclass, field
from typing import Optional
from mashumaro import field_options
from rpc.classes import BaseDictMixin

@dataclass
class GetInfoResult(BaseDictMixin):
  average_block_time: int
  block_reward: int
  block_time_target: int
  circulating_supply: int
  difficulty: str
  height: int
  maximum_supply: int
  mempool_size: int
  network: str
  stableheight: int
  top_block_hash: str
  topoheight: int
  version: str
  pruned_topoheight: Optional[int] = None
  
@dataclass
class GetBlockTemplateResult(BaseDictMixin):
  template: str
  height: int
  topoheight: int
  difficulty: str
  
@dataclass
class GetBlockAtTopoheightParams(BaseDictMixin):
  topoheight: int
  include_txs: bool
  
@dataclass
class GetBlocksAtHeightParams(BaseDictMixin):
  height: int
  include_txs: bool
  
@dataclass
class GetBlockByHashParams(BaseDictMixin):
  hash: str
  include_txs: bool
  
@dataclass
class GetTopBlockParams(BaseDictMixin):
  include_txs: bool
  
@dataclass
class GetNonceResult(BaseDictMixin):
  nonce: int
  topoheight: int
  previous_topoheight: Optional[int] = None
  
@dataclass
class VersionedNonce(BaseDictMixin):
  nonce: int
  previous_topoheight: Optional[int] = None
  
@dataclass
class GetNonceAtTopoheightParams(BaseDictMixin):
  address: str
  topoheight: int
  
@dataclass
class GetBalanceParams(BaseDictMixin):
  address: str
  asset: str
  
@dataclass
class GetBalanceAtTopoheightParams(BaseDictMixin):
  address: str
  asset: str
  topoheight: int

@dataclass
class EncryptedBalance(BaseDictMixin):
  commitment: list[int]
  handle: list[int]
  
@dataclass
class VersionedBalance(BaseDictMixin):
  balance_type: str # input, output or both
  final_balance: EncryptedBalance
  output_balance: Optional[EncryptedBalance] = None
  previous_topoheight: Optional[int] = None

@dataclass
class GetBalanceResult(BaseDictMixin):
  version: VersionedBalance
  topoheight: int

@dataclass
class GetAssetsParams(BaseDictMixin):
  Skip: Optional[int] = None
  Maximum: Optional[int] = None
  MinimumTopoheight: Optional[int] = None
  MaximumTopoheight: Optional[int] = None

@dataclass
class Asset(BaseDictMixin):
  topoheight: int
  decimals: int

@dataclass
class AssetWithData(BaseDictMixin):
  asset: str
  topoheight: int
  decimals: int
  
@dataclass
class P2PStatusResult(BaseDictMixin):
  best_topoheight: int
  max_peers: int
  our_topoheight: int
  peer_count: int
  peer_id: int
  tag: Optional[str] = None
  
@dataclass
class GetTopoheightRangeParams(BaseDictMixin):
  start_topoheight: int
  end_topoheight: int

@dataclass
class GetHeightRangeParams(BaseDictMixin):
  start_height: int
  end_height: int

@dataclass
class Block(BaseDictMixin):
  block_type: str
  cumulative_difficulty: str
  difficulty: str
  extra_nonce: str
  hash: str
  height: int
  miner: str
  nonce: int
  timestamp: int
  tips: list[str]
  total_size_in_bytes: int
  txs_hashes: list[str]
  version: int
  supply: Optional[int] = None
  dev_reward: Optional[int] = None
  miner_reward: Optional[int] = None
  reward: Optional[int] = None
  topoheight: Optional[int] = None
  total_fees: Optional[int] = None

@dataclass
class SubmitBlockParams(BaseDictMixin):
  block_template: str
  miner_work: Optional[str] = None

@dataclass
class Proof(BaseDictMixin):
  Y_0: list[int]
  Y_1: list[int]
  z_r: list[int]
  z_x: list[int]

@dataclass
class Burn(BaseDictMixin):
  asset: str
  amount: int

@dataclass
class Transfer(BaseDictMixin):
  asset: str
  destination: str
  commitment: list[int]
  sender_handle: list[int]
  receiver_handle: list[int]
  ct_validity_proof: Proof
  extra_data: Optional[list[int]] = None

@dataclass
class EqProof(BaseDictMixin):
  Y_0: list[int]
  Y_1: list[int]
  Y_2: list[int]
  z_r: list[int]
  z_s: list[int]
  z_x: list[int]

@dataclass
class SourceCommitment(BaseDictMixin):
  commitment: list[int]
  proof: EqProof
  asset: str
  
@dataclass
class Reference(BaseDictMixin):
  hash: str
  topoheight: int
  
@dataclass
class TransactionData(BaseDictMixin):
  transfers: list[Transfer]
  burn: Optional[Burn] = None

@dataclass
class Transaction(BaseDictMixin):
  hash: str
  data: TransactionData
  fee: int
  nonce: int
  source: str
  reference: Reference
  source_commitments: list[SourceCommitment]
  range_proof: list[int]
  signature: str
  version: int
  in_mempool: bool
  blocks: Optional[list[str]] = None
  executed_in_block: Optional[str] = None
  first_seen: Optional[int] = None
  
@dataclass
class GetTransactionsParams(BaseDictMixin):
  tx_hashes: list[str]

@dataclass
class MiningHistory(BaseDictMixin):
  reward: int
  
@dataclass
class BurnHistory(BaseDictMixin):
  amount: int
  
@dataclass
class OutgoingHistory(BaseDictMixin):
  to: str
  
@dataclass()
class IncomingHistory(BaseDictMixin):
  sender: str = field(metadata=field_options(alias="from"))

@dataclass
class DevFeeHistory(BaseDictMixin):
  reward: int

@dataclass
class AccountHistory(BaseDictMixin):
  topoheight: int
  block_timestamp: int
  hash: str
  mining: Optional[MiningHistory] = None
  burn: Optional[BurnHistory] = None
  outgoing: Optional[OutgoingHistory] = None
  incoming: Optional[IncomingHistory] = None
  dev_fee: Optional[MiningHistory] = None

@dataclass
class Peer(BaseDictMixin):
  id: int
  cumulative_difficulty: str
  connected_on: int
  height: int
  local_port: int
  top_block_hash: str
  addr: str
  last_ping: int
  topoheight: int
  peers: dict[str, str] # in, out or both
  version: str
  pruned_topoheight: Optional[int] = None
  tag: Optional[str] = None

@dataclass
class GetPeersResult(BaseDictMixin):
  peers: list[Peer]
  total_peers: int
  hidden_peers: int
  
@dataclass
class Fee(BaseDictMixin):
  fee_percentage: int
  height: int
  
@dataclass
class SizeOnDisk(BaseDictMixin):
  size_bytes: int
  size_formatted: str
  
@dataclass
class IsTxExecutedInBlockParams(BaseDictMixin):
  tx_hash: str
  block_hash: str
  
@dataclass
class IsAccountRegisteredParams(BaseDictMixin):
  address: str
  in_stable_height: bool
  
@dataclass
class GetDifficultyResult(BaseDictMixin):
  difficulty: str
  hashrate: str
  hashrate_formatted: str
  
@dataclass
class ValidateAddressParams(BaseDictMixin):
  address: str
  allow_integrated: bool
  
@dataclass 
class ExtractKeyFromAddressParams(BaseDictMixin):
  address: str
  tx_as_hex: bool
  
@dataclass 
class CreateMinerWorkParams(BaseDictMixin):
  template: str
  address: Optional[str] = None
  
@dataclass
class CreateMinerWorkResult(BaseDictMixin):
  miner_work: str