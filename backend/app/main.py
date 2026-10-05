from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.staticfiles import StaticFiles
from .api.routes import build_router
from .core.code_agent import CodeAgent
from .core.config import get_settings
from .core.engine import AIEngine
from .core.memory import MemorySystem
from .core.providers.local import OllamaProvider
from .core.research import ResearchService
from .core.scheduler import TaskScheduler

settings=get_settings()
memory=MemorySystem(settings.memory_db_path)
scheduler=TaskScheduler()
code_agent=CodeAgent()
provider=OllamaProvider(settings.ollama_base_url,settings.ollama_model,settings.ollama_timeout)
engine=AIEngine(provider,memory)
research=ResearchService(provider)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app=FastAPI(title=settings.app_name,version="0.1.0",lifespan=lifespan)
app.add_middleware(TrustedHostMiddleware,allowed_hosts=settings.allowed_hosts_list)
app.add_middleware(CORSMiddleware,allow_origins=settings.cors_origins_list,allow_credentials=True,allow_methods=["GET","POST","OPTIONS"],allow_headers=["*"])
app.include_router(build_router(engine,memory,scheduler,code_agent,research))

@app.get("/health")
async def health():
    return {"status":"online","system":settings.app_name,"provider":provider.name,"model":settings.ollama_model}

frontend_dir=Path(__file__).resolve().parents[2]/"frontend"
if frontend_dir.exists(): app.mount("/",StaticFiles(directory=frontend_dir,html=True),name="frontend")
