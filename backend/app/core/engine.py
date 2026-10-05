from .memory import MemorySystem
from .models import ChatResponse
from .providers.base import AIProvider

SYSTEM_PROMPT="""Você é a E.V.E.9, uma assistente de IA pessoal.
Responda em português quando o usuário falar português.
Seja objetiva, técnica quando necessário e transparente sobre limitações.
Nunca alegue ter executado uma ação que não foi realmente executada.
Alterações de arquivos ou sistema são propostas até aprovação explícita."""

class AIEngine:
    def __init__(self, provider: AIProvider, memory: MemorySystem):
        self.provider, self.memory = provider, memory
    async def chat(self, message: str, conversation_id: str) -> ChatResponse:
        memories = self.memory.recent(8)
        context = "\n".join(f"- {m.content}" for m in memories)
        prompt = message if not context else f"Contexto relevante:\n{context}\n\nUsuário:\n{message}"
        result = await self.provider.generate(prompt, SYSTEM_PROMPT)
        return ChatResponse(response=result.text,conversation_id=conversation_id,provider=result.provider,model=result.model)
