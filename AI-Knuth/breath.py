
import time
import math

riza = "Ρίζα"
parag = "Παραγοντικό"
patoma = "Πάτωμα"


# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data

#     def insert(self, data):
#         # Compare the new value with the parent node
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()

#     def searchTree(self, val):
#         # if value to be searched is found
#         if val == self.data:
#             return str(val)+" is found in the BST"
#         # if value is lesser than the value of the parent node
#         elif val < self.data:
#             # if we still need to move towards the left subtree
#             if self.leftChild:
#                 return self.leftChild.search(val)
#             else:
#                 return str(val)+" is not found in the BST"
#         # if value is greater than the value of the parent node
#         else:
#             # if we still need to move towards the right subtree
#             if self.rightChild:
#                 return self.rightChild.search(val)
#             else:
#                 return str(val)+" is not found in the BST"


# # Use the insert method to add nodes


# class Breath():
#     def __init__(self, startPoint, endPoint, maxTreeHeight):
#         self.maxTreeHeight = maxTreeHeight
#         self.startPoint = startPoint
#         self.endPoint = endPoint
#         self.queue = [startPoint]
#         self.haveChecked = []
#         self.currentPossition = 0
#         self.childrens = []
#         self.root = Node(startPoint)
#         self.sos = [{
#             "prev": -1,
#             "curr": startPoint,
#             "posList": 0,
#             "next1": -1,
#             "next2": -1,
#             "procTo": ""
#         }]
#         self.start = 0

#     def addInHaveChecked(self, checked):
#         self.haveChecked.append(checked)

#     def addNewChildrens(self, newChildrens):
#         self.childrens = newChildrens

#     def addInQueue(self, moreInQueue):
#         self.queue.extend(moreInQueue)

#     def removeFromQueue(self):
#         return self.queue.pop(0)

#     def search(self):

#         # if self.maxTreeHeight == 0:
#         #     print("fiagame")
#         #     return 0
#         # self.maxTreeHeight -= 1
#         self.currentPossition = self.removeFromQueue()
#         self.start += 1

#         if self.currentPossition == self.endPoint:
#             self.addInHaveChecked(self.currentPossition)
#             return 1
#         elif self.currentPossition not in self.haveChecked:
#             self.addInHaveChecked(self.currentPossition)
#             newChildrens = []
#             newChildrens.append(math.sqrt(self.currentPossition))
#             self.root.insert(newChildrens[0])
#             pos = -1
#             for i in range(0, len(self.sos)):
#                 if self.sos[i]["curr"] == self.currentPossition:
#                     pos = i
#                     self.sos.append({
#                         "prev":  self.sos[i]["posList"],
#                         "curr": newChildrens[0],
#                         "posList":  len(self.sos),
#                         "procTo": "τη " + riza
#                     })
#                     break

#             if isinstance(self.currentPossition, float):
#                 newChildrens.append(int(self.currentPossition))
#                 self.root.insert(newChildrens[1])
#                 self.sos.append({
#                     "prev":  self.sos[pos]["posList"],
#                     "curr": newChildrens[1],
#                     "posList":  len(self.sos),
#                     "procTo": "το " + patoma
#                 })

#             else:
#                 if self.currentPossition < 30:
#                     newChildrens.append(math.factorial(self.currentPossition))
#                     self.root.insert(newChildrens[len(newChildrens)-1])
#                     self.sos.append({
#                         "prev":  self.sos[pos]["posList"],
#                         "curr": newChildrens[len(newChildrens)-1],
#                         "posList":  len(self.sos),
#                         "procTo": "το " + parag
#                     })

#             self.addNewChildrens(newChildrens)
#             self.addInQueue(self.childrens)
#         self.search()

#     def search1(self):
#         for i in range(200):
#             self.search()


# myInput = 5
# test = Breath(4, myInput, 200)  # 960

# test.search()

# test.root.PrintTree()
# for i in test.sos:
#     print("Position in List:   "+str(i["posList"]) + "   previous: " +
#           str(i["prev"]) + "      Price:   " + str(i["curr"]) + " how : " + i["procTo"])


# i = test.start - 1
# list = []
# while (i != 0):
#     list.insert(0, test.sos[i])
#     i = test.sos[i]["prev"]

# list.insert(0, test.sos[0])

# print(
#     "Για να φτάσουμε στο " + str(myInput) + " από τον αριθμό 4. Ακολουθάμε τα εξής βήματα: ")
# for i in range(len(list) - 1):
#     print("Κάνουμε   " + list[i+1]["procTo"] +
#           ", του    " + str(list[i]["curr"]))
# print("Βρέθηκε: " + str(list[len(list)-1]["curr"]))


# -------------------------------------------------------------------------


riza = "Ρίζα"
parag = "Παραγοντικό"
patoma = "Πάτωμα"


timeout = time.time() + 60

graph = {
    4: [],
}

visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)

    while True and queue:          # Creating loop to visit each node
        if time.time() > timeout:
            print('time')
            break

        m = queue.pop(0)
        intM = m

        if (m == 17):  # 13
            print("Finds")
            break
        if isinstance(intM, float):
            # continue
            intMf = int(intM)
            # # graph[m].append({
            # #     "prev": {},
            # #     "curr": intMf,
            # #     "posList": {m, len( graph[m])},
            # #     "procTo": "kane " + patoma
            # # })
            # graph[m].append(intMf)
            # graph[intMf] = []
            if (intMf == 17):  # 13
                print("Finds")
                break

            if intMf < 170:
                intMp = math.factorial(intMf)
                graph[m].append(intMp)
                graph[intMp] = []

        else:
            if intM < 170:
                intMp = math.factorial(intM)
                graph[m].append(intMp)
                graph[intMp] = []

        if intM >= 4:
            # print(intM, " fdsfdsf   " ,math.sqrt(intM))
            intMr = math.sqrt(intM)
            # intMr = int(intMr)
            graph[m].append(intMr)
            graph[intMr] = []

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 4)    # function calling


# print(math.sqrt(  math.factorial(170)  ))

# for i in graph:
#     print(i , " : " ,graph[i])
