from linkedlist import LinkedList 
from linkedlist import Node 
import math


def addTwoLists(node1:LinkedList, node2:LinkedList):
    resultList = LinkedList()
    resultList.append(-1)
    t1, t2 = node1.head, node2.head
    current = resultList.head
    carry = 0
    while t1 or t2:
        sum = 0
        if t1:
            sum += t1.data
            t1 = t1.next
        if t2:
            sum += t2.data
            t2 = t2.next
        sum+=carry

        lsum = sum%10
        carry = math.floor(sum/10)
        print(f'carry--> {carry}')
        new_node = Node(lsum)
        current.next = new_node
        current= current.next
    if(carry):
        new_node= Node(carry)
        current.next = new_node

    resultList.head = resultList.head.next
    return resultList
# Test
ll1 = LinkedList()
ll2 = LinkedList()


ll1.append(1)
ll1.append(3)
ll1.append(7)

ll2.append(7)
ll2.append(2)
ll2.append(9)

result = addTwoLists(ll1, ll2)
result.traverse()