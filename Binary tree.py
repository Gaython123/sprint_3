class Tree:
    def __init__(self, val=None):
        # Initialize the Tree node with a value
        self.value = val

        # If the node has a value,
        # create left and right children nodes

        #if self.value - meaning self.value is in Tree (not empty)
        if self.value:
            self.left = Tree() #Create empty Nodes for the coming insertion
            self.right = Tree()

        else:
            # If the node has no value,
            # set left and right children to None
            self.left = None
            self.right = None

    # Check if the node is empty (has no value)
    def is_empty(self):
        return self.value == None #self.value == None

    # Insert a new value into the tree
    def insert(self, data):

        # If the node is empty, insert the data here
        if self.is_empty():
            self.value = data

            # Create left and right children
            # for the inserted node
            self.left = Tree()
            self.right = Tree()
            print("{} is inserted successfully".format(self.value))

        # If data is less than current node value,
        # insert into left subtree
        elif data < self.value:
            self.left.insert(data)
            return

        # If data is greater than current node value,
        # insert into right subtree
        elif data > self.value:
            self.right.insert(data)

        # If data is equal to current node value, do nothing
        elif data == self.value:
            return

T = Tree(20)
T.insert(8)
T.insert(12)
T.insert(1)
T.insert(9)
T.insert(2)