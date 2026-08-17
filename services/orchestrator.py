from packages.core import Engine

class Orchestrator:
    def __init__(self):
        self.engine = Engine()
    def add_agent(self, agent):
        self.engine.add_agent(agent)
    def remove_agent(self, agent_name):
        self.engine.remove_agent(agent_name)
    def add_task(self, task):
        self.engine.add_task(task)
    def assign_task(self, task_id, agent_name):
        self.engine.assign_task(task_id, agent_name)