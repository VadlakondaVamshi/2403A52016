class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new
    def add_beg(self,head):
        obj=Node(head)
        if self.head is None:
            self.head=obj
            return
        obj.next=self.head
        self.head=obj
    def display(self):
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
    def mid_point(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print("\nMid point is ",slow.data)
ll=LinkedList()
ll.add_beg(10)
ll.add_end(50)
ll.add_end(100)
ll.add_end(150)
ll.display()
ll.mid_point()