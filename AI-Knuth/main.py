# IMPORTS
import sys  # import system library
from time import process_time  # import time library
from mpmath import *

# Global Varialables
START_POINT = 4.0

# CHANGE THIS NUMBER
END_POINT = 13

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
                if self.children[i].parent != None:
                    self.children[i].printTree()


def bfs(queue, visited, root, target):  # function for BFS
    queue.append(root)

    while queue:

        node = None  # Node varialble for new node in tree

        currNode = queue.pop(0)  # remove first item from Queue

        visited.append(str(currNode.data))  # add this item in visited list

        bigData = currNode.data

        if (bigData == target):  # Number found.
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


def iterative_deepening_dfs_rec(currNode, target, current_depth, max_depth, visited):

    if str(currNode.data) not in visited:
        visited.append(str(currNode.data))

    bigData = currNode.data

    if bigData == target:  # Nunber Found
        return currNode, True

    if (process_time() > STOP):  # Timeout
        return None, True

    if (MAX_POINT > bigData and floor(bigData) == bigData):

        newBigData = fac(bigData)  # Make the factorial of bigData

        # if node is not in visited nodes, add the node in queue and create new Node in tree
        # if str(newBigData) not in visited:
        node = Tree(newBigData, currNode, FACTORIAL)
        if str(newBigData) not in visited:
            currNode.children.append(node)

    if bigData >= 2:  # Make sqrt if the number is is above 2

        newBigData = sqrt(bigData)  # make the sqrt of bigData

        # if node is not in visited nodes, add the node in queue and create new Node in tree
        # if str(newBigData) not in visited:
        node = Tree(newBigData, currNode, ROOT)
        if str(newBigData) not in visited:
            currNode.children.append(node)

    if floor(bigData) != bigData:  # if the number is floating point

        newBigData = floor(bigData)  # Make the floor

        # if node is not in visited nodes, add the node in queue and create new Node in tree
        # if str(newBigData) not in visited:
        node = Tree(newBigData, currNode,  FLOOR)
        if str(newBigData) not in visited:
            currNode.children.append(node)

    if current_depth == max_depth:
        # max Depth
        if len(currNode.children) > 0:
            return None, False
        else:
            return None, True

    # Recurse with all children
    bottom_reached = True

    for i in range(len(currNode.children)):

        result, bottom_reached_rec = iterative_deepening_dfs_rec(
            currNode.children[i], target, current_depth + 1, max_depth, visited)

        if result is not None:
            # βρήκαμε λύση κατεβαίνοντας στο βάθος
            return result, True

        # remove visited nodes from current depth
        if (currNode.children[i].data in visited):
            visited.remove(str(currNode.children[i].data))

        bottom_reached = bottom_reached and bottom_reached_rec

    return None, bottom_reached


# Main program
visited = []  # List for visited nodes
queue = []  # Initialize a queue

root = Tree(START_POINT, None, "")

found = True

inputChoise = int(input("1 for BFS and 2 for IDFS: "))


fileName = ""

if (inputChoise == 2):
    target = int(input("Give the target: "))

    fileName = "Iterative_Deepening_Solution"
    depth = 1

    bottom_reached = False

    while not bottom_reached:

        result, bottom_reached = iterative_deepening_dfs_rec(
            root, target, 0, 2**depth, visited)

        if result is not None:  # Number Found
            found = result
            break

        depth += 1

        visited = []  # List for visited node

    resultTime = str(process_time() - (STOP - RUNTIME))

elif (inputChoise == 1):
    target = int(input("Give the target: "))

    fileName = "Breath_First_solution"

    found = bfs(queue, visited, root, target)
    resultTime = str(process_time() - (STOP - RUNTIME))
else:
    print("Wrong input")


# Write the solution in the file
if found.__class__ == Tree:
    solutionTree = []
    while found != None:
        solutionTree.insert(0, found)
        found = found.parent

    f = open(fileName + ".txt", "w")
    if inputChoise == 2:
        f.write("Number " + str(target) +
                " found on " + str(depth) + " depth \n")
    else:
        f.write("Number " + str(target) + " found \n")
    for i in range(1, len(solutionTree)):
        f.write(solutionTree[i].createdBy + "\n")

    f.write("Time: " + resultTime[:6] + " seconds"+"\n")
    f.close()
elif inputChoise == 1 or inputChoise == 2:
    f = open(fileName + ".txt", "w")
    f.write("Number " + str(target) + " not found \n")
    f.write("Time: " + resultTime[:6] + " seconds"+"\n")
    f.close()
