#Binary tree
class BinaryTree:
    def __int__(self,name,root):
        self.name = name
        self.root = root

    def getName(self):
        return self.name
    def SetName(self,newName):
        self.name = newName
        return self.name

class BinaryTreeNode:
    def __int__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def getRightNode(self):
        return self.right
    def getLeftNode(self):
        return self.left
    def getData(self):
        return self.data

    def insertNode(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

