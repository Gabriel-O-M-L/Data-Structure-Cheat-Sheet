import heapq
# Graph structure index, for name and root
class GraphIndex:
    def __int__(self,name,root):
        self.name = name
        self.root = root

    def getName(self):
        return self.name
    def SetName(self,newName):
        self.name = newName

#Graph node structure with name and array of connected nodes
class GraphNode:
    def __int__(self,data):
        self.data = data
        self.nextNode = []

    def getNextNode(self):
        return self.nextNode
    def getData(self):
        return self.data
    def setNextNode(self,data):
        newNode = self.__int__(data)
        self.nextNode.append(newNode)
    def setData(self,data):
        self.data = data
