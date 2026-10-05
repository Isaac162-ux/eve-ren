# Arquitetura da E.V.E.9

## Princípios

**Local-first:** Ollama é o provider padrão e fica atrás de uma interface.

**Separação:** API, AI Engine, provider, memória, Code Agent, scheduler e HUD possuem responsabilidades próprias.

## Fluxo

HUD → FastAPI → AI Engine → Memory Context → Provider → HUD.

## Segurança

O Code Agent só produz propostas. Não existe execução arbitrária de código nesta versão. Uma futura camada de execução deve usar sandbox isolada, permissões explícitas, limites de recursos, logs e aprovação.

## Evolução

Provider → AI Engine → Planner → Tool Registry → Sandboxed Executor, com Memory, Permissions, Evaluation e Observability como serviços transversais.
