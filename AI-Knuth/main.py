# IMPORTS
import sys  # import system library
from time import time, process_time  # import time library
import BigNumber  # import BigNumber module
from BigNumber.BigNumber import factorial, sqrt  # import BigNumber functions

# Global Varialables
START_POINT = "4.0"

END_POINT = BigNumber.BigNumber.BigNumber("5")

# Large random number, set by creator.
MAX_POINT = BigNumber.BigNumber.BigNumber("690000000000000")

ROOT = "Ρίζα"
FACTORIAL = "Παραγοντικό"
FLOOR = "Πάτωμα"

# Limit: one mitune
STOP = process_time() + 60.0

# function for BFS


def bfs(queue, visited, graph, node):
    visited.append(node)
    queue.append(node)

    while True and queue:
        bigNode = BigNumber.BigNumber.BigNumber(
            queue.pop(0))  # New node for checking

        if (bigNode == END_POINT):  # Number found.
            return True

        if (process_time() > STOP):  # Timeout
            return False

        if (MAX_POINT > bigNode):
            try:
                # check if the bigNumber > MAX_POINT.
                # try to create the new BigNumber.
                newNode = BigNumber.BigNumber.BigNumber(factorial(bigNode))
                graph[str(bigNode)]["list"].append(str(newNode))
                if (newNode not in visited):
                    graph[str(newNode)] = {
                        "list": [],
                        "prev": str(bigNode),
                        "how": "with " + FACTORIAL
                    }
            except:
                pass

        newNode = sqrt(bigNode)  # Root of node
        newNode = newNode.__floor__()  # and floor of node in the same time
        newNode = str(newNode)

        graph[str(bigNode)]["list"].append(str(newNode))
        if (newNode not in visited):
            # check if the number is on visited.
            # There is a change that the number has already been created.
            graph[str(newNode)] = {
                "list": [],
                "prev": str(bigNode),
                "how": "with " + ROOT + " and " + FLOOR
            }

        # add visited nodes in visited list. and 'new' nodes in queue
        for neighbour in graph[str(bigNode)]["list"]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return False


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

resultTime = "0"
found = bfs(queue, visited, graph, START_POINT)
resultTime = str(process_time() - (STOP - 60))


if found:
    i = str(END_POINT)
    solution = []
    while i != START_POINT:
        solution.insert(0, [i, graph[i]["how"]])
        i = graph[i]["prev"]

    solution.insert(0, [i, graph[i]["how"]])
    print(solution[0][0])
    for i in range(1, len(solution)):
        print(solution[i][1], " ", solution[i][0])

print(resultTime[:6])
