from dataclasses import dataclass, field
from mashumaro import DataClassDictMixin

@dataclass
class ApplicationData(DataClassDictMixin):
  id: str
  name: str
  description: str
  url: str = None
  permissions: dict[str, int] = field(default_factory=dict)
  signature: str = None