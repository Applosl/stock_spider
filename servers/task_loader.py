"""
task_loader
任务加载器
"""
from config import TASKS
from tasks.task import Task


def load_task() -> bool:
    """
    加载任务
    :return:
    """
    if not isinstance(TASKS, list):
        return False
    map(_check_task_config, TASKS)
    return True


def _check_task_config(task: Task):
    """
    检查任务配置文件
    :param task:
    :return:
    """
    if not isinstance(task, Task):
        return False
    return task
