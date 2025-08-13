from linkedlist import LinkedList
from linkedlist import Node

def remove_from_back(ll:LinkedList, n):
    fast = ll.head
    slow = ll.head

    for i in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next


ll = LinkedList()
ll.append('X')
ll.append('X1')
ll.append('X2')
ll.append('X3')
ll.append('X4')
        
remove_from_back(ll, 2)
ll.traverse()