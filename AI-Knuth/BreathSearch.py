# IMPORTS
import sys  # import system library
from time import process_time  # import time library
import BigNumber  # import BigNumber module
from BigNumber.BigNumber import factorial, sqrt  # import BigNumber functions

# Global Varialables
START_POINT = "4.0"

END_POINT = BigNumber.BigNumber.BigNumber("1638")

# Large random number, set by creator.
MAX_POINT = BigNumber.BigNumber.BigNumber("690000000000000")

ROOT = "root"
FACTORIAL = "factorial"
FLOOR = "floor"

# Limit: one CPU mitune
STOP = process_time() + 120.0
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
                        str(newNode), currNode, "with " + FACTORIAL)
                    queue.append(node)
                    currNode.children.append(node)
            except:
                pass

        newNode = sqrt(bigNode)  # Root of node
        newNode = newNode.__floor__()  # and floor of node in the same time
        newNode = str(newNode)
        node = Tree(str(newNode), currNode, "with " +
                    "with " + ROOT + " and " + FLOOR)

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

resultTime = str(process_time() - (STOP - 120))


if found.__class__ == Tree:

    solutionTree = []
    while found != None:
        solutionTree.insert(0, found)
        found = found.parent

    print(solutionTree[0].node, " ->")
    for i in range(1, len(solutionTree)):
        print(solutionTree[i].process, " ", solutionTree[i].node)

# print("Steps: ", len(solutionTree), " ", resultTime[:6])
print(resultTime[:6])


# root.printTree()
