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

# Deapth first search,
    def dfs(self,root):
        if root is None:
            return None
        print(root.getData())
        for node in root.getNextNode():
            self.dfs(node)

# Breadth first search
    def bfs(self,root):
        if root is None:
            return None
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.getData())
            for node in node.getNextNode():
                queue.append(node)
# A* search
    def aStar(self,root):
        if root is None:
            return None
        heap = []
        heapq.heappush(heap,root)
        while heap:
            node = heapq.heappop(heap)
            print(node.getData())
            for node in node.getNextNode():
                heapq.heappush(heap,node)




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
