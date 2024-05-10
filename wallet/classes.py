from dataclasses import dataclass, field
from typing import Any, Optional

from mashumaro import field_options
import daemon.classes
from rpc.classes import BaseDictMixin

@dataclass
class GetAddressParams(BaseDictMixin):
  integrated_data: Optional[Any] = None

@dataclass
class SplitAddressParams(BaseDictMixin):
  address: str

@dataclass
class SplitAddressResult(BaseDictMixin):
  address: str
  integrated_data: Any
  
@dataclass
class RescanParams(BaseDictMixin):
  until_topoheight: int
  
@dataclass
class GetBalanceParams(BaseDictMixin):
  asset: str
  
@dataclass
class FeeBuilder(BaseDictMixin):
  multiplier: Optional[float] = None
  value: Optional[int] = None
  
@dataclass
class TransferOut(BaseDictMixin):
  amount: int
  asset: str
  destination: str
  extra_data: Optional[Any] = None
  
@dataclass
class TransferIn(BaseDictMixin):
  amount: int
  asset: str
  extra_data: Optional[Any] = None
  
@dataclass
class BuildTransactionParams(BaseDictMixin):
  broadcast: bool
  tx_as_hex: bool = False
  fee: Optional[FeeBuilder] = None
  transfers: Optional[list[TransferOut]] = None
  burn: Optional[daemon.classes.Burn] = None

@dataclass
class Outgoing(BaseDictMixin):
  fee: int
  nonce: int
  transfers: list[TransferOut]
  
@dataclass
class Incoming(BaseDictMixin):
  sender: str = field(metadata=field_options(alias="from"))
  transfers: list[TransferIn]
  
@dataclass
class Coinbase(BaseDictMixin):
  reward: int

@dataclass
class TransactionEntry(BaseDictMixin):
  hash: str
  topoheight: int
  outgoing: Optional[Outgoing] = None
  incoming: Optional[Incoming] = None
  coinbase: Optional[Coinbase] = None
  burn: Optional[daemon.classes.Burn] = None
  
@dataclass
class Transfer(BaseDictMixin):
  asset: str
  destination: list[int]
  commitment: list[int]
  sender_handle: list[int]
  receiver_handle: list[int]
  ct_validity_proof: daemon.classes.Proof
  extra_data: Optional[list[int]] = None

@dataclass
class TransactionData(BaseDictMixin):
  transfers: Optional[list[Transfer]] = None
  burn: Optional[daemon.classes.Burn] = None

@dataclass
class BuildTransactionResult(BaseDictMixin):
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
class EstimateFeesParams(BaseDictMixin):
  transfers: Optional[list[TransferOut]] = None
  burn: Optional[daemon.classes.Burn] = None
  
@dataclass
class ListTransactionsParams(BaseDictMixin):
  accept_incoming: bool = True
  accept_outgoing: bool = True
  accept_coinbase: bool = True
  accept_burn: bool = True
  min_topoheight: Optional[int] = None
  max_topoheight: Optional[int] = None
  address: Optional[str] = None
  
@dataclass
class SetOnlineModeParams(BaseDictMixin):
  daemon_address: str
  auto_reconnect: bool = False
  
@dataclass
class BalanceChangedResult(BaseDictMixin):
  asset: str
  balance: int