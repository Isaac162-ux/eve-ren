# E.V.E.9

> Assistente de IA pessoal, modular e orientado à privacidade.

A E.V.E.9 foi desenhada para evoluir de um assistente local para uma plataforma de IA própria. A arquitetura separa interface, API, motor de IA, memória, ferramentas e agendamento para que o provedor de modelo possa ser substituído sem reescrever o sistema.

## Arquitetura

```
HUD Web / Voz
      │
      ▼
FastAPI ──► AI Engine ──► Provider local (Ollama)
   │             │
   │             ├── Memory System (SQLite)
   │             ├── Code Agent (propostas)
   │             └── Task Scheduler
   │
   └── WebSocket / REST
```

## Estrutura

```
eve-ren/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   └── core/
│   │       └── providers/
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── assets/css/
│   ├── assets/js/
│   └── index.html
├── docs/
├── .github/workflows/
├── .env.example
├── Dockerfile
└── docker-compose.yml
```

## Execução

Copie `.env.example` para `.env`, instale Python 3.11+ e execute:

```bash
cd backend
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Abra `http://localhost:8000`.

### Modelo local

O padrão é Ollama. Instale um modelo local e mantenha o servidor acessível em `OLLAMA_BASE_URL`:

```bash
ollama pull llama3.2
```

A E.V.E.9 não exige chave de API nesse modo.

## API

- `GET /health`
- `POST /v9/chat`
- `GET/POST /v9/memory`
- `GET/POST /v9/tasks`
- `POST /v9/propose-patch`
- `GET /v9/sandbox/list`
- `WS /v9/ws/chat`
- `GET /docs`

## Voz

O HUD usa reconhecimento de fala e síntese de voz nativos do navegador quando disponíveis.

## Segurança

Segredos ficam fora do Git. O Code Agent somente gera propostas de alteração; ele não executa comandos arbitrários. Alterações futuras devem passar por sandbox isolada e aprovação explícita.

## Evolução

1. Motor local estável.
2. Memória persistente e contexto.
3. Voz e ferramentas.
4. Planner / Agent Runtime.
5. Sandbox real para tarefas autorizadas.
6. Observabilidade e avaliação.
7. Servidor próprio com autenticação.
8. API própria da E.V.E.9 para múltiplos clientes.

A arquitetura é **local-first** e evita acoplamento a um único fornecedor de modelos.
