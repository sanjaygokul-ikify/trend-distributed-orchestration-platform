import click
from services.orchestrator import Orchestrator

click.group()
def cli():
    @click.group()
    def cli_group():
        pass
    orchestrator = Orchestrator()
    @cli_group.command()
    def add_agent():
        agent_name = click.prompt('Enter agent name')
        agent_id = click.prompt('Enter agent id')
        agent = Agent(agent_name, agent_id)
        orchestrator.add_agent(agent)
    @cli_group.command()
    def remove_agent():
        agent_name = click.prompt('Enter agent name')
        orchestrator.remove_agent(agent_name)
    @cli_group.command()
    def add_task():
        task_id = click.prompt('Enter task id')
        task_name = click.prompt('Enter task name')
        task_description = click.prompt('Enter task description')
        task = Task(task_id, task_name, task_description)
        orchestrator.add_task(task)
    @cli_group.command()
    def assign_task():
        task_id = click.prompt('Enter task id')
        agent_name = click.prompt('Enter agent name')
        orchestrator.assign_task(task_id, agent_name)