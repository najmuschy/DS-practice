
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DLinkedList:
    def __init__(self):
        self.head= None
        self.tail = None
        self.len = 0

    def getLen(self):
        current=self.head
        count=0
        if self.head and self.tail==0:
            self.len=0
            return self.len
            
        while current:
            count=count+1
            current=current.next
        self.len=count    
        return self.len
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head= new_node
            self.tail = new_node
            return
        last = self.tail
        
        new_node.prev = last
        last.next = new_node
        self.tail= new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data,end="<-->")
            current = current.next
        print(None)
    def reversetraverse(self):
        current = self.tail
        while current:
            print(current.data,end="<-->")
            current = current.prev
        print(None)
    
    def insertStart(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.len = self.getLen()

    def insertPosition(self, position, data):
        new_node = Node(data)
        temp = self.head
        len = self.getLen()
        # print(f'postion {position}, len = {len}')
        if(position==0):
            self.insertStart(data)
            return
        if(position==len):
            self.append(data)
        if(position<=(len-1)):
            for i in range(position-1):
                temp = temp.next
            
            new_node.next = temp.next
            if(temp.next is not None):
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp
        self.len = self.getLen()

    def deletePosition(self, position):
        temp = self.head
        len = self.getLen()
        # print(f'postion {position}, len = {len}')

        if(position==0):
           if temp==None:
               print('List is empty')
               return
           if temp.next==None :
                self.head=None
                self.tail=None
                self.len-=1
                return
           if temp.next.next==None:
                self.head = temp.next
                self.tail =temp.next
                self.len-=1
                return
           
           temp.next.prev=None
           self.head=temp.next
           self.len-=1
           return

        if(position==(len-1)):
            self.tail.prev.next = None
            self.len-=1
        if(position<(len-1)):
            for i in range(position-1):
                temp = temp.next
            temp.next.next.prev = temp
            temp.next = temp.next.next
            self.len -=1
        
            
    def reverseList(self):
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head


                
# dll = DLinkedList()
# dll.append(1)
# dll.append(2)
# dll.append(3)

# dll.insertPosition(3,'X')
# dll.reverseList()
# dll.traverse()






