from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..core.code_agent import CodeAgent
from ..core.engine import AIEngine
from ..core.memory import MemorySystem
from ..core.models import ChatRequest, MemoryCreate, PatchRequest, TaskCreate
from ..core.scheduler import TaskScheduler

def build_router(engine: AIEngine,memory: MemorySystem,scheduler: TaskScheduler,code_agent: CodeAgent):
    router=APIRouter(prefix="/v9")
    @router.post("/chat")
    async def chat(payload: ChatRequest): return await engine.chat(payload.message,payload.conversation_id)
    @router.get("/memory")
    async def memories(): return memory.recent()
    @router.post("/memory")
    async def add_memory(payload: MemoryCreate): return memory.add(payload)
    @router.get("/tasks")
    async def tasks(): return scheduler.list()
    @router.post("/tasks")
    async def add_task(payload: TaskCreate): return scheduler.add(payload.title,payload.priority)
    @router.post("/propose-patch")
    async def propose_patch(payload: PatchRequest): return code_agent.propose(payload.path,payload.content)
    @router.get("/sandbox/list")
    async def sandbox_list(): return {"files":[],"message":"Sandbox segura ainda não foi habilitada."}
    @router.websocket("/ws/chat")
    async def websocket_chat(websocket: WebSocket):
        await websocket.accept()
        try:
            while True:
                response=await engine.chat(await websocket.receive_text(),"websocket")
                await websocket.send_json(response.model_dump(mode="json"))
        except WebSocketDisconnect: pass
    return router
