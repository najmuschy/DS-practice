from doubly_linkedlist import DLinkedList
from doubly_linkedlist import Node


def find_sum_pairs(head, tail, sum):

    pairs = []
    left = head 
    right =tail
    print(right.data)
    while left.data<=right.data and left!=right :
        print(f'left {left.data} right {right.data}')
        if left.data+right.data == sum:
            pairs.append((left.data, right.data)) 
            left = left.next
            right = right.prev
        elif left.data+right.data< sum:
            left =  left.next
        elif left.data+right.data > sum:
            right = right.prev
        
    return pairs

dll = DLinkedList()

dll.append(1)
dll.append(2)
dll.append(2)
dll.append(2)
dll.append(3)
dll.append(4)

pairs = find_sum_pairs(dll.head, dll.tail, 4)

print(pairs)