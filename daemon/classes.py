from dataclasses import dataclass, field
from typing import Optional

from mashumaro import DataClassDictMixin, field_options

@dataclass
class GetInfoResult(DataClassDictMixin):
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
class GetBlockTemplateResult(DataClassDictMixin):
  template: str
  height: int
  topoheight: int
  difficulty: str
  
@dataclass
class GetBlockAtTopoheightParams(DataClassDictMixin):
  topoheight: int
  include_txs: bool
  
@dataclass
class GetBlocksAtHeightParams(DataClassDictMixin):
  height: int
  include_txs: bool
  
@dataclass
class GetBlockByHashParams(DataClassDictMixin):
  hash: str
  include_txs: bool
  
@dataclass
class GetTopBlockParams(DataClassDictMixin):
  include_txs: bool
  
@dataclass
class GetNonceResult(DataClassDictMixin):
  nonce: int
  topoheight: int
  previous_topoheight: Optional[int] = None
  
@dataclass
class VersionedNonce(DataClassDictMixin):
  nonce: int
  previous_topoheight: Optional[int] = None
  
@dataclass
class GetNonceAtTopoheightParams(DataClassDictMixin):
  address: str
  topoheight: int
  
@dataclass
class GetBalanceParams(DataClassDictMixin):
  address: str
  asset: str
  
@dataclass
class GetBalanceAtTopoheightParams(DataClassDictMixin):
  address: str
  asset: str
  topoheight: int

@dataclass
class EncryptedBalance(DataClassDictMixin):
  commitment: list[int]
  handle: list[int]
  
@dataclass
class VersionedBalance(DataClassDictMixin):
  balance_type: str # input, output or both
  final_balance: EncryptedBalance
  output_balance: Optional[EncryptedBalance] = None
  previous_topoheight: Optional[int] = None

@dataclass
class GetBalanceResult(DataClassDictMixin):
  version: VersionedBalance
  topoheight: int

@dataclass
class GetAssetsParams(DataClassDictMixin):
  Skip: Optional[int] = None
  Maximum: Optional[int] = None
  MinimumTopoheight: Optional[int] = None
  MaximumTopoheight: Optional[int] = None

@dataclass
class Asset(DataClassDictMixin):
  topoheight: int
  decimals: int

@dataclass
class AssetWithData(DataClassDictMixin):
  asset: str
  topoheight: int
  decimals: int
  
@dataclass
class P2PStatusResult(DataClassDictMixin):
  best_topoheight: int
  max_peers: int
  our_topoheight: int
  peer_count: int
  peer_id: int
  tag: Optional[str] = None
  
@dataclass
class GetTopoheightRangeParams(DataClassDictMixin):
  start_topoheight: int
  end_topoheight: int

@dataclass
class GetHeightRangeParams(DataClassDictMixin):
  start_height: int
  end_height: int

@dataclass
class Block(DataClassDictMixin):
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
  total_size_in_bytes: int
  txs_hashes: list[str]
  version: int
  total_fees: Optional[int] = None

@dataclass
class SubmitBlockParams(DataClassDictMixin):
  block_template: str
  miner_work: Optional[str] = None

@dataclass
class Proof(DataClassDictMixin):
  Y_0: list[int]
  Y_1: list[int]
  z_r: list[int]
  z_x: list[int]

@dataclass
class Burn(DataClassDictMixin):
  asset: str
  amount: int

@dataclass
class Transfer(DataClassDictMixin):
  asset: str
  destination: str
  commitment: list[int]
  sender_handle: list[int]
  receiver_handle: list[int]
  ct_validity_proof: Proof
  extra_data: Optional[list[int]] = None

@dataclass
class EqProof(DataClassDictMixin):
  Y_0: list[int]
  Y_1: list[int]
  Y_2: list[int]
  z_r: list[int]
  z_s: list[int]
  z_x: list[int]

@dataclass
class SourceCommitment(DataClassDictMixin):
  commitment: list[int]
  proof: EqProof
  asset: str
  
@dataclass
class Reference(DataClassDictMixin):
  hash: str
  topoheight: int
  
@dataclass
class TransactionData(DataClassDictMixin):
  transfers: list[Transfer]
  burn: Optional[Burn] = None

@dataclass
class Transaction(DataClassDictMixin):
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
class GetTransactionsParams(DataClassDictMixin):
  tx_hashes: list[str]

@dataclass
class MiningHistory(DataClassDictMixin):
  reward: int
  
@dataclass
class BurnHistory(DataClassDictMixin):
  amount: int
  
@dataclass
class OutgoingHistory(DataClassDictMixin):
  to: str
  
@dataclass()
class IncomingHistory(DataClassDictMixin):
  sender: str = field(metadata=field_options(alias="from"))

@dataclass
class DevFeeHistory(DataClassDictMixin):
  reward: int

@dataclass
class AccountHistory(DataClassDictMixin):
  topoheight: int
  block_timestamp: int
  hash: str
  mining: Optional[MiningHistory] = None
  burn: Optional[BurnHistory] = None
  outgoing: Optional[OutgoingHistory] = None
  incoming: Optional[IncomingHistory] = None
  dev_fee: Optional[MiningHistory] = None

@dataclass
class Peer:
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
class GetPeersResult(DataClassDictMixin):
  peers: list[Peer]
  total_peers: int
  hidden_peers: int
  
@dataclass
class Fee(DataClassDictMixin):
  fee_percentage: int
  height: int
  
@dataclass
class SizeOnDisk(DataClassDictMixin):
  size_bytes: int
  size_formatted: str
  
@dataclass
class IsTxExecutedInBlockParams(DataClassDictMixin):
  tx_hash: str
  block_hash: str
  
@dataclass
class IsAccountRegisteredParams(DataClassDictMixin):
  address: str
  in_stable_height: bool
  
@dataclass
class GetDifficultyResult(DataClassDictMixin):
  difficulty: str
  hashrate: str
  hashrate_formatted: str
  
@dataclass
class ValidateAddressParams(DataClassDictMixin):
  address: str
  allow_integrated: bool
  
@dataclass 
class ExtractKeyFromAddressParams(DataClassDictMixin):
  address: str
  tx_as_hex: bool
  
@dataclass 
class CreateMinerWorkParams(DataClassDictMixin):
  template: str
  address: Optional[str] = None
  
@dataclass
class CreateMinerWorkResult(DataClassDictMixin):
  miner_work: str