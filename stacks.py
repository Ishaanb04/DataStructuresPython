from node import Node

class StackIterator:
    def __init__(self, top_node):
        self._current = top_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.get_current() == None:
            raise StopIteration
        data = self.get_current().get_data()
        self.set_current(self.get_current().get_next())
        return data
    
    def get_current(self):
        return self._current

    def set_current(self, new_node):
        self._current = new_node

class Stack:
    def __init__(self, limit = 1000):
        self._top = None
        self.limit = limit
        self._size = 0

    def __iter__(self):
        return StackIterator(self.get_top())
    
    def __repr__(self):
        representation = '['
        current = self.get_top()
        if current == None:
            representation += ']'
        else: 
            while current.get_next() != None:
                representation += f'{current.get_data()}, '
                current = current.get_next()
            representation += f'{current.get_data()}]'
        return representation
        
    def get_top(self):
        return self._top
    
    def get_size(self):
        return self._size

    def increase_size(self):
        self._size += 1
    
    def decrease_size(self):
        self._size -= 1

    def set_top(self, new_node):
        self._top = new_node

    def is_allowed(self):
        return self.get_size() < self.limit

    def peek(self):
        return self.get_top().get_data()
    
    def is_empty(self):
        return self.get_size() == 0

    def push(self, data):
        new_node = Node(data)
        if self.is_allowed():
            if self.get_top() == None:
                self.set_top(new_node)
            else:
                new_node.set_next(self.get_top())
                self.set_top(new_node)
            self.increase_size()
        return self

    def pop(self):
        if self.get_top() == None:
            print('Stack is Empty')
            return None
        else:
            node = self.get_top()
            self.set_top(self.get_top().get_next())
            self.decrease_size()
            return node.get_data()