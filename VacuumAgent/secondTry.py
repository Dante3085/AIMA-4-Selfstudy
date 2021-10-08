
import random
import sys

# Folgendes weiß der Agent...
# 1. Wie viel Dreck er bereits bereinigt hat.
# 2. Ob das Feld, auf dem er steht sauber oder dreckig ist?
#
# Was kann der Agent mit diesen Informationen tun, um besser als zufällig
# seine Umgebung vollständig zu säubern?
class Agent:
    def __init__(self):
        self.cleanedUpDirt = 0

    def act(self, state):
        if state == "C":
            return "MOVE_RANDOMLY"
        elif state == "D":
            self.cleanedUpDirt += 1
            return "CLEAN"

    # Kann man hier irgendwo das Konzept einer reward function einbringen?
    # Beziehungsweise eine Heuristik abhängig vom Zustand der Umgebung, die 
    # der Agent nutzen kann, um bessere Entscheidungen zu treffen?

class Environment:
    def __init__(self, width, height, agent) -> None:
        self.env = []
        self.randomizeEnvironment(width, height)
        self.agent = agent
        self.agentLocation = [random.randint(0, width - 1), random.randint(0, height - 1)]
        
    def randomizeEnvironment(self, width, height):
        for i in range(0, height):
            self.env.append([])
            for j in range(0, width):
                rndBit = random.randint(0, 1)
                if (rndBit == 0):
                    self.env[i].append("C")
                else:
                    self.env[i].append("D")

    def toString(self):
        strRep = ""
        for i in range(0, len(self.env[0])):
            for j in range(0, len(self.env)):
                if [i,j] == self.agentLocation:
                    strRep += "A "
                else:
                    strRep += self.env[i][j] + " "
            strRep += "\n"
        return strRep

    def tick(self):
        nextAgentAction = self.agent.act(self.env[self.agentLocation[0]][self.agentLocation[1]])
        if (nextAgentAction == "CLEAN"):
            self.env[self.agentLocation[0]][self.agentLocation[1]] = "C"

        # Note: The agent can also move left, or any other direction, when there is no more left to go.
        #       The result would be that the agent doesn't move at all.
        # TODO: Agent shouldn't be able to move into a wall. This takes a lot of unnecessary time when
        #       ticking the environment.
        elif (nextAgentAction == "MOVE_RANDOMLY"):
            rndNumber = random.randint(0, 3)

            # move left
            if rndNumber == 0:
                self.agentLocation[0] -= 1

            # move up
            elif rndNumber == 1:
                self.agentLocation[1] -= 1

            # move right
            elif rndNumber == 2:
                self.agentLocation[0] += 1

            # move down
            elif rndNumber == 3:
                self.agentLocation[1] += 1

            self.__checkAgentBounds()

    def __checkAgentBounds(self):
        '''If any of the Agents coordinates are outside of the enviornment's bounds, this method
           corrects those to the closest value in the direction they went of the bounds.'''

        if self.agentLocation[0] < 0:
            self.agentLocation[0] = 0
        if self.agentLocation[0] >= len(self.env[0]):
            self.agentLocation[0] = len(self.env[0]) - 1
        
        if self.agentLocation[1] < 0:
            self.agentLocation[1] = 0
        if self.agentLocation[1] >= len(self.env):
            self.agentLocation[1] = len(self.env) - 1

envWidth = 3
envHeight = 3
if len(sys.argv) > 1:
    envWidth = int(sys.argv[1])
    envHeight = int(sys.argv[2])

agent = Agent()  
env = Environment(envWidth, envHeight, agent)
print("INITIAL ENVIRONMENT\n" + env.toString() + "\n-----------")

while (True):
    inp = input("Press enter to tick the environment!")
    env.tick()
    print(env.toString() + "\n----------")