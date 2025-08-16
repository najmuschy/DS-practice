from linkedlist import LinkedList
from linkedlist import Node


def sort(head: Node) -> Node :
    if head == None or head.next == None:
        return head
    
    newHead = sort(head.next)
    front = head.next
    front.next = head
    head.next= None
    return newHead

def isPalindrome(head: Node) -> bool:
    temp = head
    fast = head
    slow= head

    if temp.next ==None :
        return True
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    newHead = sort(slow.next)
    tempNewHead = newHead
    while tempNewHead:
        if temp.data!= tempNewHead.data:
            sort(newHead)
            return False
        tempNewHead = tempNewHead.next
        temp=temp.next


    sort(newHead)
    return True

ll = LinkedList()
ll.append(2)
ll.append(1)
ll.append(5)
ll.append(1)


isPal = isPalindrome(ll.head)

print(isPal)
ll.traverse()
