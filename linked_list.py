import math

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
    
    def get_data(self):
        return self._data
    
    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node

class LinkedListIterator:
    def __init__(self, head_node):
        self._current = head_node

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

class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __iter__(self):
        return LinkedListIterator(self.get_head())

    def __repr__(self):
        representation = '['
        current = self.get_head()
        if current == None:
            print('Empty linked list')
            representation += ']'
        else:
            while current.get_next() != None:
                representation += f'{current.get_data()}, '
                current = current.get_next()
            representation += f'{current.get_data()}]'
        return representation

    def get_head(self):
        return self._head

    def set_head(self, node):
        self._head = node

    def get_size(self):
        return self._size

    def increase_size(self):
        self._size += 1
    
    def decrease_size(self):
        self._size -= 1

    def add_start(self, data):
        new_node = Node(data)
        
        if self.get_head() == None:
            self.set_head(new_node)
        else:
            new_node.set_next(self.get_head())
            self.set_head(new_node)
        self.increase_size()
        return self
    
    def add_end(self, data):
        new_node = Node(data)
        current = self.get_head()
        if self.get_head() == None:
            self.set_head(new_node)
        else:
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)
        self.increase_size()
        return self

    def print_elements(self):
        current = self.get_head()
        if current == None:
            print('Empty linked list')
        else:
            while current != None:
                print(current.get_data())
                current = current.get_next()
    
    def remove_start(self):

        if self.get_head() == None:
            return self
        elif self.get_head().get_next() == None:
            self.set_head(None)
        else:
            self.set_head(self.get_head().get_next())
        self.decrease_size()
        return self

    def remove_end(self):
        current = self.get_head()
        prev = None
        if self.get_head() == None:
            return self
        elif self.get_head().get_next() == None:
            self.set_head(None)
        else:   
            while current.get_next() != None:
                prev = current
                current = current.get_next()
            prev.set_next(None)
        self.decrease_size()
        return self

    def get_middle(self):
        the_size = self.get_size()
        is_even = the_size % 2 == 0
        
        if self.get_head() == None:
            return None
        elif self.get_head().get_next() == None:
            return self.get_head()
        else:
            slow_pointer = self.get_head()
            fast_pointer = self.get_head()
            prev = None
            while fast_pointer != None and fast_pointer.get_next() != None:
                prev = slow_pointer
                slow_pointer = slow_pointer.get_next()
                fast_pointer = fast_pointer.get_next().get_next()
            if is_even:
                return (prev.get_data(), slow_pointer.get_data())
            else:
                return slow_pointer.get_data()
        
the_list = LinkedList()
the_list.add_end(10).add_end(20).add_end(30).add_end(40).add_end(50).add_end(60)
print(the_list)
print(the_list.get_middle())