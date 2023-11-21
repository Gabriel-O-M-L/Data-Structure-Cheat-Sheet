class Sorting:
    def __init__(self, data):
        self.data = data
        self.length = len(data)

    def bubbleSort(self):
        for i in range(self.length):
            for j in range(self.length - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def selectionSort(self):
        for i in range(self.length):
            min_index = i
            for j in range(i + 1, self.length):
                if self.data[min_index] > self.data[j]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

    def insertionSort(self):
        for i in range(1, self.length):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key

    def mergeSort(self):
        if self.length > 1:
            mid = self.length // 2
            left = self.data[:mid]
            right = self.data[mid:]
            left_sort = Sorting(left)
            right_sort = Sorting(right)
            left_sort.mergeSort()
            right_sort.mergeSort()
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.data[k] = left[i]
                    i += 1
                else:
                    self.data[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                self.data[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                self.data[k] = right[j]
                j += 1
                k += 1

    def quickSort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.quickSort(low, pivot - 1)
            self.quickSort(pivot + 1, high)

    def partition(self,low,high):
        i = low - 1
        pivot = self.data[high]
        for j in range(low, high):
            if self.data[j] < pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1