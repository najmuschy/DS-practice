from linkedlist import LinkedList
from linkedlist import Node


def findLoopLength(fast, slow):
    count =1
    while fast.next!=slow:
        count+=1
        fast = fast.next
    return count


def loop(head):

    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast==slow:
            length = findLoopLength(fast, slow)
            return length
    return 0

ll=LinkedList()
ll.append(1)
ll.append(2)
connect1 =ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
connect2 = ll.append(7)

connect2.next = connect1

print(loop(ll.head))


