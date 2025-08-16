from linkedlist import LinkedList
from linkedlist import Node

def findKthNode(head, k):
    while k>1:
        k-=1
        head = head.next
    return head


def rotate(head, k):
    temp = head
    len =1
    while temp.next:
        temp= temp.next
        len+=1
    tail = temp
    if(k%len==0):
        return head
    n= len - (k%len)
    kthNode =  findKthNode(head, n)
    tail.next = head
    head = kthNode.next
    kthNode.next = None

    return head


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.head = rotate(ll.head, 2)

ll.traverse()
