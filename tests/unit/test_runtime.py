import unittest
from services.orchestrator import Orchestrator

class TestRuntime(unittest.TestCase):
    def test_add_agent(self):
        orchestrator = Orchestrator()
        agent = Agent('agent1', 'id1')
        orchestrator.add_agent(agent)
        self.assertEqual(len(orchestrator.engine.agents), 1)
    def test_remove_agent(self):
        orchestrator = Orchestrator()
        agent = Agent('agent1', 'id1')
        orchestrator.add_agent(agent)
        orchestrator.remove_agent('agent1')
        self.assertEqual(len(orchestrator.engine.agents), 0)