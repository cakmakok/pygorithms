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


llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(6)
llist.append(6)


print(llist.display())
llist.remove_dups()
print(llist.display())

