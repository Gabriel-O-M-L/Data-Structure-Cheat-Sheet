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
    def getRoot(self):
        return self.root
# All orderef traversal onganized in one function divided by type
    def OrderTraversal(self,root,type):
        if type == "inOrder":
            if root:
                self.OrderTraversal(root.getLeftNode())
                print(root.getData())
                self.OrderTraversal(root.getRightNode())
        elif type == "preOrder":
            if root:
                print(root.getData())
                self.OrderTraversal(root.getLeftNode())
                self.OrderTraversal(root.getRightNode())
        elif type == "postOrder":
            if root:
                self.OrderTraversal(root.getLeftNode())
                self.OrderTraversal(root.getRightNode())
                print(root.getData())
    def searchNode(self,data):
        if data == self.root.getData():
            return self.root
    def deapthFirstSearch(self,root):
        if root is None:
            return None
        print(root.getData())
        for node in root.getNextNode():
            self.dfs(node)

#Binary tree node structure with data and left and right nodes
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

