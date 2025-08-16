from doubly_linkedlist import DLinkedList
from doubly_linkedlist import Node

def removeDupli(head):
    temp =  head
    nextNode = head.next

    while temp.next:
        if temp.data == nextNode.data:
            nextNode= nextNode.next
        else:
            temp.next = nextNode
            nextNode.prev= temp
            temp= nextNode
            nextNode= nextNode.next
    return head
    
dll = DLinkedList()

dll.append(1)
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(3)
dll.append(4)

dll.head = removeDupli(dll.head)

dll.traverse()