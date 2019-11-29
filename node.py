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