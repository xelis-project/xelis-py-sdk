from dataclasses import dataclass
from mashumaro import DataClassDictMixin
from mashumaro.config import BaseConfig

@dataclass
class BaseDictMixin(DataClassDictMixin):
  class Config(BaseConfig):
    omit_none = True # don't serialize parameters with None