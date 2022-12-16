# IMPORTS
from time import process_time  # import time library
import BigNumber  # import BigNumber module
from BigNumber.BigNumber import factorial, sqrt  # import BigNumber functions

# Global Varialables
START_POINT = "4.0"

# CHANGE THIS NUMBER
END_POINT = BigNumber.BigNumber.BigNumber("6")
# 597
# Large random number, set by creator.
MAX_POINT = BigNumber.BigNumber.BigNumber("690000000000000")

ROOT = "root"
FACTORIAL = "factorial"
FLOOR = "floor"

RUNTIME = 60.0
# Limit: one CPU mitune
STOP = process_time() + RUNTIME
# process_time - It does not include the waiting time for resources


class Tree():
    def __init__(self, node, parent, process):
        self.node = node
        self.children = []
        self.parent = parent
        self.process = process

    def printTree(self):
        print(self.node)
        for i in range(len(self.children)):
            self.children[i].printTree()


def check(currNode, visited):
    for i in visited:
        if currNode == i.node:
            return False
    return True


def bfs(queue, visited, root):  # function for BFS
    visited.append(root)
    queue.append(root)

    while queue:
        node = None
        currNode = queue.pop(0)
        visited.append(currNode)

        bigNode = BigNumber.BigNumber.BigNumber(
            currNode.node)  # New node for checking

        if (bigNode == END_POINT):  # Number found.
            return currNode

        if (process_time() > STOP):  # Timeout
            return False

        if (MAX_POINT > bigNode):
            try:
                # check if the bigNumber > MAX_POINT.
                # try to create the new BigNumber.
                newNode = BigNumber.BigNumber.BigNumber(factorial(bigNode))

                # if node is not in visited nodes, add the node in queue
                if check(str(newNode), visited):
                    node = Tree(
                        str(newNode), currNode, FACTORIAL)
                    queue.append(node)
                    currNode.children.append(node)
            except:
                pass

        newNode = sqrt(bigNode)  # Root of node
        newNode = newNode.__floor__()  # and floor of node in the same time
        newNode = str(newNode)
        node = Tree(str(newNode), currNode, ROOT + " " + FLOOR)

        # if node is not in visited nodes, add the node in queue
        if check(str(newNode), visited):
            currNode.children.append(node)
            queue.append(node)

    return False


# -------------Main-------------
# Initialize varialables

root = Tree(START_POINT, None, "")  # Create Tree


visited = []  # List for visited nodes
queue = []  # Initialize a queue

found = bfs(queue, visited, root)

resultTime = str(process_time() - (STOP - RUNTIME))


if found.__class__ == Tree:

    solutionTree = []
    while found != None:
        solutionTree.insert(0, found)
        found = found.parent

    # Add solution in file
    f = open("Breath_First_solution.txt", "w")
    for i in range(1, len(solutionTree)):
        if (ROOT in solutionTree[i].process):
            f.write(solutionTree[i].node + "  " + ROOT + FLOOR + "\n")
            # f.write(FLOOR + "\n")
        else:
            f.write(solutionTree[i].node + "  " + FACTORIAL + "\n")

    f.write("Time: " + resultTime[:6] + " seconds"+"\n")
    f.close()
