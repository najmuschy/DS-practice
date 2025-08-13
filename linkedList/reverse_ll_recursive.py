from linkedlist import LinkedList
from linkedlist import Node

def sortRecursive(head):
    
    if head==None or head.next==None:
        return head
    
    newHead = sortRecursive(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newHead

ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.head = sortRecursive(ll.head)

ll.traverse()
