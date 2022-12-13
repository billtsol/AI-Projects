# IMPORTS
import mpmath
import sys  # import system library
from time import time  # import time library
import math  # import math library
import BigNumber  # import BigNumber module
from BigNumber.BigNumber import factorial, sqrt  # import BigNumber functions

# Global Varialables
START_POINT = "4.0"

END_POINT = BigNumber.BigNumber.BigNumber("13")

MAX_POINT = BigNumber.BigNumber.BigNumber("668950291344913")

ROOT = "Ρίζα"
FACTORIAL = "Παραγοντικό"
FLOOR = "Πάτωμα"

START_TIME = time() + 60.0


# function for BFS
def bfs(queue, visited, graph, node):
    visited.append(node)
    queue.append(node)

    while time() < START_TIME and queue:
        bigNode = BigNumber.BigNumber.BigNumber(queue.pop(0))

        if (bigNode == END_POINT):  # Number found
            return True

        if (MAX_POINT > bigNode):
            try:
                newNode = BigNumber.BigNumber.BigNumber(factorial(bigNode))
                graph[str(bigNode)]["list"].append(str(newNode))
                graph[str(newNode)] = {
                    "list": [],
                    "prev": str(bigNode),
                    "how": "with " + FACTORIAL
                }
            except:
                pass

        newNode = str(sqrt(bigNode))
        if newNode not in visited:
            graph[str(bigNode)]["list"].append(str(newNode))
            graph[str(newNode)] = {
                "list": [],
                "prev": str(bigNode),
                "how": "with " + ROOT + " and " + FLOOR
            }

        for neighbour in graph[str(bigNode)]["list"]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# -------------Main-------------
# Initialize varialables
graph = {
    START_POINT: {
        "list": [],
        "prev": "-1",
        "how": ""
    },
}


visited = []  # List for visited nodes
queue = []  # Initialize a queue

bfs(queue, visited, graph, START_POINT)

i = str(END_POINT)
solution = []
while i != START_POINT:
    solution.insert(0, [i, graph[i]["how"]])
    i = graph[i]["prev"]

solution.insert(0, [i, graph[i]["how"]])

print(solution[0][0])
for i in range(1, len(solution)):
    print(solution[i][1], " ", solution[i][0])
