from dataclasses import dataclass, field
from itertools import count

@dataclass(order=True)
class ScheduledTask:
    priority: int
    id: int = field(compare=False)
    title: str = field(compare=False)
    status: str = field(default="queued", compare=False)

class TaskScheduler:
    def __init__(self):
        self._ids, self._tasks = count(1), []
    def add(self, title: str, priority: int = 5) -> ScheduledTask:
        task = ScheduledTask(priority=priority,id=next(self._ids),title=title)
        self._tasks.append(task); self._tasks.sort(); return task
    def list(self): return list(self._tasks)
