# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Function to insert in BST
    def leftChildInsert(self, data):
        if self.leftChild:
            # if we still need to move towards the left subtree
            self.leftChild.rightChildInsert(data)
        else:
            self.leftChild = Node(data)
            return

    def rightChildInsert(self, data):
        if self.rightChild:
            # if we still need to move towards the left subtree
            self.rightChild.leftChildInsert(data)
        else:
            self.rightChild = Node(data)
            return

    # function to print a BST
    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.data),
        if self.rightChild:
            self.rightChild.PrintTree()


# Creating root node
root = Node("riza")
# Inserting values in BST
root.leftChildInsert("protoaristera")
root.rightChildInsert("protodeksia")

print(root.leftChild.data)

# printing BST
# root.PrintTree()
