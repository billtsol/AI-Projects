# IMPORTS
import mpmath
import sys  # import system library
from time import time  # import time library
import math  # import math library
import BigNumber  # import BigNumber module
from BigNumber.BigNumber import factorial, sqrt  # import BigNumber functions

# Global Varialables
START_POINT = "4"
END_POINT = "5"

ROOT = "Ρίζα"
FACTORIAL = "Παραγοντικό"
FLOOR = "Πάτωμα"

START_TIME = time() + 60
# function for BFS


def bfs(queue, visited, graph, node):
    visited.append(node)
    queue.append(node)

    while time() < START_TIME and queue:
        node = queue.pop(0)
        bigNode = BigNumber.BigNumber.BigNumber(node)
        positionString = node

        if (positionString == END_POINT):
            print("FIND")
            break
        # if isinstance(bigNode, float):
        #     newChildren = str(bigNode.__floor__())
        #     graph[positionString].append(newChildren)
        #     graph[newChildren] = []
        # else:
        newChildren = str(factorial(bigNode))
        graph[positionString].append(newChildren)
        graph[newChildren] = []

        newChildren = str(sqrt(bigNode))
        graph[positionString].append(newChildren)
        graph[newChildren] = []

        for i in graph:
            print(i, " : ", graph[i])
        print()
        print()
        print()

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# -------------Main-------------
# Initialize varialables
graph = {
    START_POINT: [],
}

visited = []  # List for visited nodes
queue = []  # Initialize a queue


bfs(queue, visited, graph, START_POINT)

for i in graph:
    print(i, " : ", graph[i])
