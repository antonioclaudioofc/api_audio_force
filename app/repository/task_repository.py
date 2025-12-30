from core.store import TASKS
from domain.download.enums import TaskStatus


class TaskRepository:

    def create(self, task_id: str):
        TASKS[task_id] = {"status": TaskStatus.QUEUED}

    def update_status(self, task_id: str, status: TaskStatus):
        TASKS[task_id]["status"] = status

    def set_error(self, task_id: str, error: str):
        TASKS[task_id]["status"] = TaskStatus.ERROR
        TASKS[task_id]["error"] = error

    def exists(self, task_id: str):
        return task_id in TASKS
