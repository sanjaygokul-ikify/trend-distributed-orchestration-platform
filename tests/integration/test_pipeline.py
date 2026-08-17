import unittest
from services.orchestrator import Orchestrator
from packages.core import Engine, Agent, Task

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine()
        agent = Agent('agent1', 'id1')
        engine.add_agent(agent)
        task = Task('id1', 'task1', 'description1')
        engine.add_task(task)
        engine.assign_task('id1', 'agent1')
        self.assertEqual(len(engine.task_assignments), 1)
        orchestrator = Orchestrator()
        orchestrator.add_agent(agent)
        orchestrator.add_task(task)
        orchestrator.assign_task('id1', 'agent1')
        self.assertEqual(len(orchestrator.engine.task_assignments), 1)