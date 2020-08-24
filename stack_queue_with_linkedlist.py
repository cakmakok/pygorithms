class Node:
    def __init__(self, value=None):
        self.value =value
        self.next = None

    @property
    def next(self):
        return self.next

    def __repr__(self):
        return str(self.value)

class Stack:
    def __init__(self, top = None):
        self.top = top

    def push(self, node):
        if self.top:
            current_top_element = self.top
            node.next = current_top_element
            self.top = node
        else:
            self.top = node

    def peek(self):
        return self.top

    def pop(self):
        if self.top:
            element_to_be_popped = self.top
            new_top_element = element_to_be_popped.next
            self.top = new_top_element
            return element_to_be_popped
        return None

class Queue:
    def __init__(self, node=None):
        self.start = node
        self.end = node

    def add(self, node):
        if self.end:
            current_end = self.end
            current_end.next = node
            self.end = node
        else:
            self.end = node
            self.start = node

    def remove(self):
        if self.start:
            current_start = self.start
            new_start = self.start.next
            self.start =new_start
            return current_start
        else:
            return None

