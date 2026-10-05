import httpx
from .base import AIProvider, ProviderResponse

class OllamaProvider(AIProvider):
    name = "ollama"
    def __init__(self, base_url: str, model: str, timeout: float = 90.0):
        self.base_url, self.model, self.timeout = base_url.rstrip("/"), model, timeout
    async def generate(self, prompt: str, system: str | None = None) -> ProviderResponse:
        payload = {"model": self.model, "prompt": prompt, "stream": False}
        if system: payload["system"] = system
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()
            data = response.json()
        return ProviderResponse(data.get("response", "").strip() or "Não recebi uma resposta do modelo local.", self.name, self.model)
