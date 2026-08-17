import unittest
from packages.core import Engine, Agent, Task

class TestCore(unittest.TestCase):
    def test_add_agent(self):
        engine = Engine()
        agent = Agent('agent1', 'id1')
        engine.add_agent(agent)
        self.assertEqual(len(engine.agents), 1)
    def test_remove_agent(self):
        engine = Engine()
        agent = Agent('agent1', 'id1')
        engine.add_agent(agent)
        engine.remove_agent('agent1')
        self.assertEqual(len(engine.agents), 0)
    def test_add_task(self):
        engine = Engine()
        task = Task('id1', 'task1', 'description1')
        engine.add_task(task)
        self.assertEqual(len(engine.tasks), 1)
    def test_assign_task(self):
        engine = Engine()
        agent = Agent('agent1', 'id1')
        engine.add_agent(agent)
        task = Task('id1', 'task1', 'description1')
        engine.add_task(task)
        engine.assign_task('id1', 'agent1')
        self.assertEqual(len(engine.task_assignments), 1)