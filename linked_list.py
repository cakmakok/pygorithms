class Node:
    def __init__(self, value=None):
        self.value =value
        self.next_node = None

    @property
    def next(self):
        return self.next_node

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        cur = self.head
        while cur.next_node is not None:
            cur = cur.next_node

        cur.next_node = Node(value)

    def length(self):
        counter = 0
        cur = self.head
        while cur.next_node is not None:
            cur = cur.next_node
            counter +=1
        return counter

    def display(self):
        l = []
        cur = self.head
        while cur.next_node is not None:
            cur = cur.next_node
            l.append(cur.value)
        return l

    def get_node(self, index):
        if index >= self.length():
            raise IndexError

        cur = self.head
        for _ in range(0,index+1):
            cur = cur.next_node
        return cur

    def get(self, index):
        return self.get_node(index).value

    def delete(self, index):
        node = self.get_node(index)
        node_before = self.get_node(index - 1)
        node_before.next_node = node.next_node

    def get_head(self):
        return self.head

    def has_next(self,index):
        return bool(self.get_node(index).next_node)

    def remove_dups(self):
        from collections import defaultdict
        items = defaultdict(int)

        cur = self.get_node(0)
        previous_node = None
        while cur:
            if items[cur.value]:
                previous_node.next_node=cur.next_node
            else:
                items[cur.value] += 1
                previous_node = cur
            cur = cur.next_node


    def remove_dups(self):
        from collections import defaultdict
        items = defaultdict(int)

        cur = self.get_node(0)
        previous_node = None
        while cur:
            if items[cur.value]:
                previous_node.next_node=cur.next_node
            else:
                items[cur.value] += 1
                previous_node = cur
            cur = cur.next_node

    def remove_dups_without_buffer(self):
        cur = self.get_node(0)

        while cur:
            cur_value = cur.value
            next_node = cur.next_node
            while next_node:
                if next_node.value == cur_value:
                    cur.next_node = next_node.next_node
                next_node = next_node.next_node
            cur = cur.next_node

    def nth_to_last(self, n):
        cur1 = self.get_node(0)
        cur2 = self.get_node(0)

        for _ in range(0,n):
            cur1=cur1.next_node

        while cur1.next_node:
            cur1 = cur1.next_node
            cur2 = cur2.next_node
        return cur2.value

from random import randint
llist = LinkedList()

for _ in range(0,10):
    llist.append(randint(0,10))

print(llist.display())
llist.remove_dups()
print(llist.display())
