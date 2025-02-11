class MyArrayList:
    def __init__(self):
        self.data = []
        self.size = 0
        
    def append(self,value):
        self.data.append(value)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.data.pop()