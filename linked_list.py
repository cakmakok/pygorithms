class Node:
    def __init__(self, value=None):
        self.value =value
        self.next_node = None

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

    def __get_node(self, index):
        if index >= self.length():
            raise IndexError

        cur = self.head
        for _ in range(0,index+1):
            cur = cur.next_node
        return  cur

    def get(self, index):
        return self.__get_node(index).value

    def delete(self, index):
        node = self.__get_node(index)
        node_before = self.__get_node(index-1)
        node_before.next_node = node.next_node


llist = LinkedList()
llist.append(4)
llist.append(5)
llist.append(6)
print(llist.length())
print(llist.display())
llist.delete(2)
print(llist.display())
