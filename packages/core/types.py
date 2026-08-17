from dataclasses import dataclass
from typing import List

@dataclass
class Agent:
    name: str
    id: str

@dataclass
class Task:
    id: str
    name: str
    description: str

@dataclass
class TaskAssignment:
    task_id: str
    agent_name: str
