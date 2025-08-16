from linkedlist import LinkedList
from linkedlist import Node

def reverse(head):
    
    if head.next==None:
        return head
    newHead = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None

    return newHead

def find_kth_node(temp, k):
    
    while temp and k>1:
        k= k-1
        temp=temp.next
    return temp

def reverse_kth(head, k):
    temp = head
    kthNode = head

    prevNode = None

    
    while temp:
        kthNode = find_kth_node(temp, k)
        if kthNode==None:
            if prevNode==None: 
                break
            else:
                prevNode.next = temp 
                break
        next_node = kthNode.next
        kthNode.next = None
        newHead = reverse(temp)
        if temp == head:
            prevNode = temp
            head= newHead
            temp = next_node
        else:
            prevNode.next = newHead
            prevNode = temp
            temp = next_node
    return head

ll = LinkedList()

ll.append(3)
ll.append(2)
ll.append(1)
ll.append(6)
ll.append(5)
ll.append(4)
ll.append(9)
ll.append(8)
ll.append(7)

ll.head = reverse_kth(ll.head, 3)

ll.traverse()




