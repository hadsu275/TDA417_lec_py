class Search:

    def __init__(self):
        self.arr = []
        
    def addElement(self, elm):
        self.arr.append(elm)

    def linear_search(self, target):
        for i in self.arr:
            if i == target:
                return True
            
        return False
    
    def linear(self, target):
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i
            
            
        return -1
    
        
s = Search()
s.addElement(1)
s.addElement(2)
s.addElement(3)
s.addElement(4)
s.addElement(5)
s.addElement(6)
s.addElement(7)
s.addElement(8)

print(s.linear_search(2))
print(s.linear(5))





