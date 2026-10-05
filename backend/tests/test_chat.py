import pytest
from app.core.engine import AIEngine
from app.core.memory import MemorySystem
from app.core.models import MemoryCreate
from app.core.providers.base import AIProvider, ProviderResponse

class FakeProvider(AIProvider):
    name="test"
    async def generate(self,prompt,system=None): return ProviderResponse("Resposta de teste",self.name,"fake")

@pytest.mark.asyncio
async def test_engine_uses_memory_context(tmp_path):
    memory=MemorySystem(str(tmp_path/"memory.db"))
    memory.add(MemoryCreate(content="Nome do projeto: E.V.E.9",category="project"))
    response=await AIEngine(FakeProvider(),memory).chat("Qual é o projeto?","test")
    assert response.response=="Resposta de teste"
    assert response.provider=="test"
