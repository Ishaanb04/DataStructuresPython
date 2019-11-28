class Node:
    def __init__(self, data, next = None):      
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def set_next(self, link_next):
        self.next = link_next

class Stack:
    def __init__(self, limit = 1000):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_data()
        else:
            print('Stack is empty')

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print('Stack is already full')

    def pop(self):
        if not self.is_empty():
            item = self.top_item
            self.top_item = item.get_next()
            self.size -= 1
            return item.get_data()
            
        else:
            print('Stack is empty!')
    
    def has_space(self):
        return self.limit >self.size

    def is_empty(self):
        return self.size == 0 
