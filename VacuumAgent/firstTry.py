
from enum import Enum
import time

class AgentAction(Enum):
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    SUCK = 3

class EnvironmentStatus(Enum):
    CLEAN = 1
    DIRTY = 2

class EnvironmentLocation(Enum):
    A = 1
    B = 2

class VacuumAgent:
    def __init__(self) -> None:
        pass
    
    def act(self, location: EnvironmentLocation, status: EnvironmentStatus) -> AgentAction:
        if status == EnvironmentStatus.DIRTY: return AgentAction.SUCK
        elif location == EnvironmentLocation.A: return AgentAction.MOVE_RIGHT
        elif location == EnvironmentLocation.B: return AgentAction.MOVE_LEFT

class VacuumEnvironment:
    def __init__(self, agent: VacuumAgent) -> None:
        self.agent = agent
        self.environment = {
            EnvironmentLocation.A: EnvironmentStatus.DIRTY,
            EnvironmentLocation.B: EnvironmentStatus.DIRTY
        }
        self.agentLocation = EnvironmentLocation.A
        
    def tick(self) -> str:
        '''Advances the environment one timestep/Allows the agent to take one action
           and then returns the state of the entire enviornment as a string.'''

        nextAgentAction = self.agent.act(self.agentLocation, self.environment[self.agentLocation])

        if nextAgentAction == AgentAction.SUCK:
            self.environment[self.agentLocation] = EnvironmentStatus.CLEAN
        elif nextAgentAction == AgentAction.MOVE_LEFT:
            self.agentLocation = EnvironmentLocation.A
        elif nextAgentAction == AgentAction.MOVE_RIGHT:
            self.agentLocation = EnvironmentLocation.B

        envString = ""
        for location in self.environment:
            if self.environment[location] == EnvironmentStatus.CLEAN: 
                envString += "C "
            elif self.environment[location] == EnvironmentStatus.DIRTY: 
                envString += "D "

        return envString
    
agent = VacuumAgent()
env = VacuumEnvironment(agent)

while (True):
    inp = input("Advance one timestep...")
    print(env.tick())
