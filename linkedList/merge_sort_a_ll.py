from linkedlist import LinkedList  
from linkedlist import Node

def merge(head1, head2):
    dummyNode  = Node(-1)
    temp = dummyNode

    while head1 or head2:
        if head1 == None:
            temp.next = head2
            break
        elif head2== None:
            temp.next = head1
            break
        elif head1.data < head2.data:
            temp.next = head1
            temp = temp.next
            head1= head1.next
        elif head2.data< head1.data:
            temp.next= head2
            temp = temp.next
            head2 = head2.next
    
    return dummyNode.next


def findMidNode(head):
    fast= head
    slow = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    return slow

def merge_sort(head):
    if head==None or head.next==None:
        return head
    midNode = findMidNode(head)

    leftHead = head
    rightHead = midNode.next
    midNode.next = None

    leftHead =merge_sort(leftHead)
    rightHead = merge_sort(rightHead)
    return merge(leftHead, rightHead)
ll = LinkedList()
ll1 = LinkedList()

ll.append(8)
ll.append(3)
ll.append(7)
ll.append(5)
ll.append(1)
ll.append(9)

ll.head = merge_sort(ll.head)
ll.traverse()

