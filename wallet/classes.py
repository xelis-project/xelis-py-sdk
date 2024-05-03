from dataclasses import dataclass, field
from typing import Optional
import daemon.classes

from mashumaro import DataClassDictMixin, field_options

@dataclass
class GetAddressParams(DataClassDictMixin):
  integrated_data: Optional[any] = None

@dataclass
class SplitAddressParams(DataClassDictMixin):
  address: str

@dataclass
class SplitAddressResult(DataClassDictMixin):
  address: str
  integrated_data: any
  
@dataclass
class RescanParams(DataClassDictMixin):
  until_topoheight: int
  
@dataclass
class GetBalanceParams(DataClassDictMixin):
  asset: str
  
@dataclass
class FeeBuilder(DataClassDictMixin):
  multiplier: Optional[float] = None
  value: Optional[int] = None
  
@dataclass
class TransferOut(DataClassDictMixin):
  amount: int
  asset: str
  destination: str
  extra_data: Optional[any] = None
  
@dataclass
class TransferIn(DataClassDictMixin):
  amount: int
  asset: str
  extra_data: Optional[any] = None
  
@dataclass
class BuildTransactionParams(DataClassDictMixin):
  transfers: list[TransferOut]
  broadcast: bool
  tx_as_hex: bool
  fee_builder: Optional[FeeBuilder] = None
  burn: Optional[daemon.classes.Burn] = None

@dataclass
class Outgoing(DataClassDictMixin):
  fee: int
  nonce: int
  transfers: list[TransferOut]
  
@dataclass
class Incoming(DataClassDictMixin):
  sender: str
  transfers: list[TransferIn]
  
@dataclass
class Coinbase(DataClassDictMixin):
  reward: int

@dataclass
class TransactionEntry(DataClassDictMixin):
  hash: str
  topoheight: int
  outoing: Optional[Outgoing] = None
  incoming: Optional[Incoming] = None
  coinbase: Optional[Coinbase] = None
  burn: Optional[daemon.classes.Burn] = None
  
@dataclass
class Transfer(DataClassDictMixin):
  asset: str
  destination: list[int]
  commitment: list[int]
  sender_handle: list[int]
  receiver_handle: list[int]
  ct_validity_proof: daemon.classes.Proof
  extra_data: Optional[list[int]] = None

@dataclass
class TransactionData(DataClassDictMixin):
  transfers: list[Transfer]
  burn: Optional[daemon.classes.Burn] = None

@dataclass
class BuildTransactionResult(DataClassDictMixin):
  data: TransactionData
  fee: int
  hash: str
  nonce: int
  range_proof: list[int]
  reference: daemon.classes.Reference
  signature: str
  source: list[int]
  source_commitments: list[daemon.classes.SourceCommitment]
  tx_as_hex: str
  version: str
  
@dataclass
class EstimateFeesParams:
  transfers: Optional[list[TransferOut]] = None
  burn: Optional[daemon.classes.Burn] = None
  
@dataclass
class ListTransactionsParams:
  accept_incoming: bool = True
  accept_outgoing: bool = True
  accept_coinbase: bool = True
  accept_burn: bool = True
  min_topoheight: Optional[int] = None
  max_topoheight: Optional[int] = None
  address: Optional[str] = None