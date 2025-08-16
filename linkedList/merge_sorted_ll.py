from linkedlist import LinkedList
from linkedlist import Node

def merge_sorted(head1, head2):
    t1 = head1
    t2 = head2

    dummyNode =  Node(-1)
    temp = dummyNode
    while t1 or t2:
        if t1 == None:
            temp.next= t2
            break
        elif t2== None:
            temp.next = t1
            break
        if t1.data<=t2.data:
            temp.next = t1
            temp = temp.next
            t1 = t1.next
        elif t2.data<=t2.data:
            temp.next= t2
            temp =  temp.next
            t2 = t2.next



    head = dummyNode.next
    return head

ll1= LinkedList()
ll2= LinkedList()

ll1.append(1)
ll1.append(1)
ll1.append(4)
ll1.append(6)
ll1.append(6)
ll1.append(8)

ll2.append(2)
ll2.append(3)
ll2.append(3)
ll2.append(5)
ll2.append(7)
ll2.append(7)

ll2.head = merge_sorted(ll1.head, ll2.head)

ll2.traverse()