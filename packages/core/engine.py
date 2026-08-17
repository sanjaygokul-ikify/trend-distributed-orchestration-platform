from typing import List, Dict
import logging
from .types import Agent, Task, TaskAssignment
from .exceptions import TaskAssignmentError, AgentError

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self):
        self.agents: List[Agent] = []
        self.tasks: Dict[str, Task] = {}
        self.task_assignments: Dict[str, TaskAssignment] = {}

    def add_agent(self, agent: Agent):
        if not isinstance(agent, Agent):
            raise AgentError('Invalid agent')
        self.agents.append(agent)
        logger.info(f'Added agent {agent.name}')

    def remove_agent(self, agent_name: str):
        for agent in self.agents:
            if agent.name == agent_name:
                self.agents.remove(agent)
                logger.info(f'Removed agent {agent_name}')
                return
        raise AgentError('Agent not found')

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise TaskAssignmentError('Invalid task')
        self.tasks[task.id] = task
        logger.info(f'Added task {task.id}')

    def assign_task(self, task_id: str, agent_name: str):
        if task_id not in self.tasks:
            raise TaskAssignmentError('Task not found')
        for agent in self.agents:
            if agent.name == agent_name:
                task_assignment = TaskAssignment(task_id, agent_name)
                self.task_assignments[task_id] = task_assignment
                logger.info(f'Assigned task {task_id} to agent {agent_name}')
                return
        raise AgentError('Agent not found')

    def get_task_assignments(self, agent_name: str):
        task_assignments = []
        for task_id, task_assignment in self.task_assignments.items():
            if task_assignment.agent_name == agent_name:
                task_assignments.append(task_assignment)
        return task_assignments

    def get_agent_tasks(self, agent_name: str):
        agent_tasks = []
        for task_id, task_assignment in self.task_assignments.items():
            if task_assignment.agent_name == agent_name:
                agent_tasks.append(self.tasks[task_id])
        return agent_tasks
