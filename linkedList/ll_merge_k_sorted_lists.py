from linkedlist import LinkedList
from linkedlist import Node
import heapq, itertools

def merge(listh):
    h=[]
    counter = itertools.count()
    dummyNode = Node(-1)
    temp  = dummyNode

    for i in listh:
        heapq.heappush(h, (i.data, next(counter), i))

    while h:
        minV = heapq.heappop(h)
        temp.next = minV[2]
        if minV[2].next:
            heapq.heappush(h, (minV[2].next.data, next(counter), minV[2].next))
        temp = temp.next
    return dummyNode.next

        


ll = LinkedList()
ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()

ll.append(1)
ll.append(3)
ll1.append(5)
ll1.append(8)
ll2.append(7)
ll3.append(7)
heads = [ll.head, ll1.head, ll2.head, ll3.head]
ll.head = merge(heads)

ll.traverse()


