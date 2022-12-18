# IMPORTS
import sys  # import system library
from time import process_time  # import time library
import BigNumber  # import BigNumber module
from BigNumber.BigNumber import factorial, sqrt  # import BigNumber functions

LIMIT = 8
# Global Varialables
START_POINT = "4.0"

# CHANGE THIS NUMBER
END_POINT = BigNumber.BigNumber.BigNumber("6")

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
            if self.children[i].parent != None:
                self.children[i].printTree()


def check(currNode, visited):
    for i in visited:
        if currNode == i.node:
            return False
    return True


def iterative_deepening_dfs(start, target):
    visited = []
    depth = 1
    bottom_reached = False  # Δείχνει εάν φτάσαμε στο πάτωμα του δέντρου
    while not bottom_reached:
        result, bottom_reached = iterative_deepening_dfs_rec(
            start, target, 0, depth, visited)

        if result is not None:
            print("Increasing depth to " + str(depth))
            # Βρέθηκε ο κόμβος που ψάχναμε
            print(visited)
            return result

        # Δεν βρήκαμε λύση, και αυξάνουμε το βάθος του δέντρου
        depth *= 2
        # if depth == LIMIT:
        #     break
    # Το bottom_reached εγινε True.
    # Δεν βρήκαμε τον κόμβο και δεν υπήρχαν άλλοι κόμβοι που έχουν ακόμα παιδιά για εξερεύνηση σε μεγαλύτερο βάθος.
    return None


def iterative_deepening_dfs_rec(node, target, current_depth, max_depth, visited):
    # print(node.node)
    if node.node not in visited:
        visited.append(node.node)

    bigNode = BigNumber.BigNumber.BigNumber(node.node)
    if bigNode == target:  # βρήκαμε λύση
        print("Found the node we're looking for!")
        return node, True

    if (process_time() > STOP):  # τέλειωσε ο χρόνος
        print("time")
        sys.exit()

    if (MAX_POINT > bigNode):
        try:
            # check if the bigNumber > MAX_POINT.
            # try to create the new BigNumber.
            newNode = BigNumber.BigNumber.BigNumber(factorial(bigNode))
            t = Tree(str(newNode), node, FACTORIAL)
        except:
            newNode = sqrt(bigNode)
            t = Tree(str(newNode), node, ROOT + " " + FLOOR)
    else:
        newNode = sqrt(bigNode)
        t = Tree(str(newNode), node, ROOT + " " + FLOOR)

    if t.node not in visited:
        node.children.append(t)

    newNode = sqrt(bigNode)
    t = Tree(str(newNode), node, ROOT + " " + FLOOR)
    if t.node not in visited:
        node.children.append(t)

    if current_depth == max_depth:
        # Φτάσαμε στο μέγιστο βάθος του δέντρου.
        if len(node.children) > 0:
            # Δεν έχουμε ελέγξει όλα τα παιδιά ακόμα
            return None, False
        else:
            return None, True

    # Recurse with all children
    bottom_reached = True
    for i in range(len(node.children)):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(
            node.children[i], target, current_depth + 1, max_depth, visited)

        if result is not None:
            # βρήκαμε λύση κατεβαίνοντας στο βάθος
            return result, True

        if (node.children[i].node in visited): # Διαγραφη του 
            visited.remove(node.children[i].node)

        bottom_reached = bottom_reached and bottom_reached_rec

    # είδαμε όλα τα παιδιά στο βάθος και δεν βρήκαμε λύση
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
