import heapq
class HeapUtil():
    def __init__(self, x):
        self.x = x

    def __cmp__(self, other):
        if self.x<other.x:
            return -1
        elif self.x == other.x:
            return 0
        else:
            return 1

    def maxheappush(heap, item):
        heapq.heappush(heap, HeapUtil(item))

    def maxheappop(heap):
        return heapq.heappop(heap).x
