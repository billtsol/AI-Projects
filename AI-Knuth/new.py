# IMPORTS
import sys  # import system library
from time import process_time  # import time library
import BigNumber  # import BigNumber module
from BigNumber.BigNumber import factorial, sqrt  # import BigNumber functions

LIMIT = 6
# Global Varialables
START_POINT = "4.0"

# CHANGE THIS NUMBER
END_POINT = BigNumber.BigNumber.BigNumber("1")

# Large random number, set by creator.
MAX_POINT = BigNumber.BigNumber.BigNumber("690000000000000")

ROOT = "root"
FACTORIAL = "factorial"
FLOOR = "floor"

RUNTIME = 60.0
# Limit: one CPU mitune
STOP = process_time() + RUNTIME
# process_time - It does not include the waiting time for resources

# bathos 18


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


def iterative_deepening_dfs(start, target):
    # Start by doing DFS with a depth of 1, keep doubling depth until we reach the "bottom" of the tree or find the node we're searching for
    depth = 1
    bottom_reached = False  # Variable to keep track if we have reached the bottom of the tree
    while not bottom_reached:
        # One of the "end nodes" of the search with this depth has to still have children and set this to False again
        result, bottom_reached = iterative_deepening_dfs_rec(
            start, target, 0, depth)
        if result is not None:
            print("Increasing depth to " + str(depth))

            # We've found the goal node while doing DFS with this max depth
            return result

        # We haven't found the goal node, but there are still deeper nodes to search through
        depth *= 2
        # print("Increasing depth to " + str(depth))

    # Bottom reached is True.
    # We haven't found the node and there were no more nodes that still have children to explore at a higher depth.
    return None


def iterative_deepening_dfs_rec(node, target, current_depth, max_depth):
    # print("Visiting Node " + node.node)
    bigNode = BigNumber.BigNumber.BigNumber(node.node)
    if bigNode == target:
        # We have found the goal node we we're searching for
        print("Found the node we're looking for!")
        return node, True

    if (process_time() > STOP):
        print("time")
        sys.exit()

    if (MAX_POINT > bigNode):
        try:
            # check if the bigNumber > MAX_POINT.
            # try to create the new BigNumber.
            newNode = BigNumber.BigNumber.BigNumber(factorial(bigNode))
            t = Tree(str(newNode), node, FACTORIAL)
            # node = Tree(str(newNode), currNode, "with " + FACTORIAL)
        except:
            newNode = sqrt(bigNode)
            t = Tree(str(newNode), node, ROOT + " " + FLOOR)

    else:
        newNode = sqrt(bigNode)
        t = Tree(str(newNode), node, ROOT + " " + FLOOR)

    node.children.append(t)

    newNode = sqrt(bigNode)
    t = Tree(str(newNode), node, ROOT + " " + FLOOR)
    node.children.append(t)

    if current_depth == max_depth:
        # print("Current maximum depth reached, returning...")
        # We have reached the end for this depth...
        if len(node.children) > 0:
            # ...but we have not yet reached the bottom of the tree
            return None, False
        else:
            return None, True

    # Recurse with all children
    bottom_reached = True
    for i in range(len(node.children)):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(node.children[i], target, current_depth + 1,
                                                                 max_depth)
        if result is not None:
            # We've found the goal node while going down that child
            return result, True
        bottom_reached = bottom_reached and bottom_reached_rec

    # We've gone through all children and not found the goal node
    return None, bottom_reached


trees = Tree(START_POINT, None, "")
found = iterative_deepening_dfs(trees, END_POINT)
resultTime = str(process_time() - (STOP - RUNTIME))


if found.__class__ == Tree:

    solutionTree = []
    while found != None:
        solutionTree.insert(0, found)
        found = found.parent

    # Add solution in file
    f = open("Iterative_Deepening_Solution.txt", "w")
    for i in range(1, len(solutionTree)):
        if (ROOT in solutionTree[i].process):
            f.write(solutionTree[i].node + "  " + ROOT + FLOOR + "\n")
            # f.write(FLOOR + "\n")
        else:
            f.write(solutionTree[i].node + "  " + FACTORIAL + "\n")

    f.write("Time: " + resultTime[:6] + " seconds"+"\n")
    f.close()
