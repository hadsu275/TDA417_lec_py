class Sort:

    def __init__(self):
        self.arr = []

    def addElement(self, elm):
        if isinstance(elm, list):
            self.arr.extend(elm)
        else:
            self.arr.append(elm)

    def selection_sort(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

s = Sort()
s.addElement(64)
s.addElement(25)
s.addElement(12)

s.addElement(22)
s.addElement(11)
print("Unsorted array:", s.arr)
s.selection_sort()
print("Sorted array:", s.arr)
