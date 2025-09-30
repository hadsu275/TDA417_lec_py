class Stack:
    def __init__(self):
        self.stack = []

    # denna metod lägg till element i stacken
    def push(self, elm):
        self.stack.append(elm)
    # denna ta bort den element från stacken vilket den som ligger top i stacken
    # eller den som man ligger sist i stacken
    def pop(self):
        if self.isEmpty():
            print("stacken is empty")
            return
        self.stack.pop()
    # denna metod är att kolla den top element vilket det är sista element man lägga till 
    def peek(self):
        if self.isEmpty():
            print("stacken is empty")
            return
        return self.stack[-1]
    # denna metot kollar om stacken är empty eller inte
    def isEmpty(self):
        return len(self.stack) == 0
    # denna metod return size på stacken
    def size_stack(self):
        return len(self.stack)
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.isEmpty())
print(s.stack)
print(s.pop())
print(s.stack)
print(s.size_stack())