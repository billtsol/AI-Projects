# IMPORTS
from time import process_time  # import time library
import BigNumber  # import BigNumber module
from BigNumber.BigNumber import factorial  # import BigNumber functions

from mpmath import *
# Global Varialables
START_POINT = 4.0

# CHANGE THIS NUMBER
END_POINT = 5

# Large random number, set by creator.
MAX_POINT = 9999999  # 9.999.999

ROOT = "Root"
FACTORIAL = "Factorial"
FLOOR = "Floor"

RUNTIME = 60.0
# Limit: one CPU mitune
STOP = process_time() + RUNTIME
# process_time - It does not include the waiting time for resources


class Tree():
    def __init__(self, data, parent, createdBy):
        self.data = data
        self.children = []
        self.parent = parent
        self.createdBy = createdBy

    def printTree(self):
        print(self.data)
        for i in range(len(self.children)):
            if self.children[i].parent != None:
                self.children[i].printTree()


def bfs(queue, visited, root):  # function for BFS
    queue.append(root)

    while queue:

        node = None  # Node varialble for new node in tree

        currNode = queue.pop(0)  # remove first item from Queue

        visited.append(str(currNode.data))  # add this item in visited list

        bigData = currNode.data

        if (bigData == END_POINT):  # Number found.
            return currNode

        if (process_time() > STOP):  # Timeout
            return False

        if (MAX_POINT > bigData and floor(bigData) == bigData):

            newBigData = fac(bigData)  # Make the factorial of bigData

            # if node is not in visited nodes, add the node in queue and create new Node in tree
            if str(newBigData) not in visited:
                node = Tree(newBigData, currNode, FACTORIAL)
                queue.append(node)
                currNode.children.append(node)

        if bigData >= 2:  # Make sqrt if the number is is above 2

            newBigData = sqrt(bigData)  # make the sqrt of bigData

            # if node is not in visited nodes, add the node in queue and create new Node in tree
            if str(newBigData) not in visited:
                node = Tree(newBigData, currNode, ROOT)
                currNode.children.append(node)
                queue.append(node)

        if floor(bigData) != bigData:  # if the number is floating point

            newBigData = floor(bigData)  # Make the floor

            # if node is not in visited nodes, add the node in queue and create new Node in tree
            if str(newBigData) not in visited:
                node = Tree(newBigData, currNode,  FLOOR)
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
        if (ROOT in solutionTree[i].createdBy):
            f.write(str(solutionTree[i].data) + "  " + ROOT + "\n")
        elif FLOOR in solutionTree[i].createdBy:
            f.write(str(solutionTree[i].data) + "  " + FLOOR + "\n")
        else:
            f.write(str(solutionTree[i].data) + "  " + FACTORIAL + "\n")

    f.write("Time: " + resultTime[:6] + " seconds"+"\n")
    f.close()
