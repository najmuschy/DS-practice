from linkedlist import LinkedList
from linkedlist import Node

def detect_loop_position(head):
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow =slow.next

        if fast == slow:
            slow = head
            while slow!=fast:
                slow=slow.next
                fast = fast.next
            return slow
    return 0;


ll=LinkedList()
ll.append(1)
ll.append(2)
connect1 =ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
connect2 = ll.append(7)

connect2.next = connect1

print(detect_loop_position(ll.head).data)
