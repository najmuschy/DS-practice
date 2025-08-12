from linkedlist import LinkedList
from linkedlist import Node

def rearrange(ll:LinkedList):
    odd = ll.head
    even = ll.head.next
    tempEven = ll.head.next

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = tempEven

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

rearrange(ll)
ll.traverse()

