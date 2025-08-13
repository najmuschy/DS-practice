from linkedlist import LinkedList
from linkedlist import Node


def sort(ll:LinkedList):
    temp = ll.head#0
    zeroNode = Node(-1)
    oneNode = Node(-1)
    twoNode = Node(-1)

    zero = zeroNode
    one = oneNode
    two = twoNode
    while temp:
        if temp.data==0:
            zero.next = temp #3 -1-->0
            zero = zero.next #3  0
        elif temp.data==1: 
            one.next = temp #1 -1-->1 
            one = one.next #1 1  
        else:
            two.next = temp #2 -1-->2
            two = two.next #2 2
        temp = temp.next#1 temp=2 #2 temp=0 #3temp = None
    if oneNode.next!=None:
        zero.next = oneNode.next
    else:
        zero.next = twoNode.next
    one.next = twoNode.next
    two.next =  None
    ll.head = zeroNode.next
    



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(0)
ll.append(1)
ll.append(2)
ll.append(0)
ll.append(0)
ll.append(0)


sort(ll)
ll.traverse()