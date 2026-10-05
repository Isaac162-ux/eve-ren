from .providers.base import AIProvider

class ResearchService:
    def __init__(self, provider: AIProvider):
        self.provider = provider

    async def research(self, topic: str):
        prompt = f"""Faça uma análise estruturada sobre o tema abaixo.
Não invente fontes ou fatos. Deixe claro quando algo precisar de verificação externa.

Tema: {topic}

Entregue:
1. Resumo
2. Pontos principais
3. Perguntas em aberto
4. Próximos passos para validação"""
        return await self.provider.generate(prompt, "Você é o módulo de pesquisa da E.V.E.9.")
