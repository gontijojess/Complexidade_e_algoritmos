import sys
sys.stdout.reconfigure(encoding='utf-8')

class ArraySorter:
    def __init__(self, array):
        self.array = array
        self.nItems = len(array)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def bidirectionalBubbleSort(self):
        left = 0
        right = self.nItems - 1
        
        while left < right:
            for i in range(left, right):
                if self.array[i] > self.array[i + 1]:
                    self.swap(i, i + 1)
            right -= 1
            
            for i in range(right, left, -1):
                if self.array[i] < self.array[i - 1]:
                    self.swap(i, i - 1)
            left += 1

array = [5, 3, 8, 6, 2, 7, 4, 1]
sorter = ArraySorter(array)

print("Antes da ordenação:")
print(sorter.array)

sorter.bidirectionalBubbleSort()

print("Depois da ordenação:")
print(sorter.array)