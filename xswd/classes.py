from dataclasses import dataclass, field
  
@dataclass
class ApplicationData:
  id: str
  name: str
  description: str
  url: str = None
  permissions: dict[str, int] = field(default_factory=dict)
  signature: str = None