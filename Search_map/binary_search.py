class BinarySearch:
    def __init__(self):
        self.arr = []
        
    def addElement(self, elm):
        if isinstance(elm, list):
            self.arr.extend(elm)
        else:
            self.arr.append(elm)
        
        self.arr.sort()
    
    def search(self, target):
        left, right = 0, len(self.arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
s = BinarySearch()
s.addElement(1)     
s.addElement(2)
s.addElement(3)
s.addElement(4)
s.addElement(5)
s.addElement([6, 7, 8])
print(s.search(2))
print(s.search(5))  