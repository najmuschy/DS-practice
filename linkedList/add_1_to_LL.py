from linkedlist import LinkedList
from linkedlist import Node


def helper(head):
    temp = head
    if temp ==None:
        return 1
    
    carry = helper(temp.next)
    temp.data =  temp.data + carry 
    if temp.data<10:
        carry = 0
        return 0;
    temp.data = 0
    return 1


def add(head):
    temp = head
    carry = helper(head)
    if carry==1:
        newHead = Node(carry)
        newHead.next=temp
        return newHead
    return temp

ll = LinkedList()
ll.append(9)
ll.append(9)
ll.append(9)
ll.append(8)

ll.head = add(ll.head)

ll.traverse()

