from linkedlist import LinkedList
from linkedlist import Node

def findIntersection(head1, head2):
    temp1 = head1
    temp2 =  head2 


    while(temp1!= temp2):

        if temp1==temp2:
            
            return temp1
        
        if temp1 == None :
            temp1 = head2
            
        if temp2 == None:
            temp2 = head1
        
        temp1 = temp1.next
        temp2 =  temp2.next

    return temp1

# ll1 = LinkedList()
# ll2 = LinkedList()

# ll1.append(1)
# connect2 =ll1.append(3)
# ll1.append(4)

# ll2.append(1)
# connect1 =ll2.append(2)

# print(connect1)
# connect1.next = connect2

# result  = findIntersection(ll1.head, ll2.head)

# print(result.data)