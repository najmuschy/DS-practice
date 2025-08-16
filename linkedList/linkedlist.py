import math 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        return last.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print(current)

    def insertBeginning(self, data):
        temp_node = self.head
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = temp_node
        self.head = new_node

    def insertPosition(self, position, data):
        new_node = Node(data)
        current = self.head
        temp = self.head
        len = 0
        while current:
            len = len + 1
            current = current.next
        print(position)
        if position == 0:
            self.insertBeginning(data)
            return

        if position < len:
            for i in range(position - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

# ll = LinkedList()

# ll.append(1)
# ll.append(1)
# ll.append(1)
# ll.append(1)

# ll.traverse()