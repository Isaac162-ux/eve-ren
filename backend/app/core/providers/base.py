from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class ProviderResponse:
    text: str
    provider: str
    model: str

class AIProvider(ABC):
    name: str
    @abstractmethod
    async def generate(self, prompt: str, system: str | None = None) -> ProviderResponse:
        raise NotImplementedError
