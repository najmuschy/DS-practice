from doubly_linkedlist import DLinkedList
from doubly_linkedlist import Node

def deleteOccurance(head ,key):

    temp = head
    prevNode = None
    nextNode = temp.next
    while temp:

        if temp.data == key:
            if temp==head:
                head = head.next
                print(head.data)
            else:
                nextNode = temp.next
                prevNode = temp.prev
                if nextNode: nextNode.prev = prevNode
                if prevNode: prevNode.next = nextNode
                temp = temp.next
            

        else:
            temp = temp.next

    return head


dll = DLinkedList()


dll.append(10)
dll.append(10)
dll.append(3)
dll.append(10)
dll.append(4)
dll.append(10)


dll.head = deleteOccurance(dll.head, 10)

dll.traverse()