class Node:
    def __init__(self,data):
        self.data=data           #defining the structure of the node
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=self.last=None
    
    def insertLeft(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.last=n
            self.last.next=self.head
        else:
            n.next=self.head
            self.head=n
    def insertRight(self,data):
        n=Node(data)
        if self.head==None:
            self.head=self.last=n
            self.last.next=self.head
        else:
            self.last.next=n
            self.last=n
            self.last.next=self.head
            
    def deleteRight(self):
        if self.head==None:
            print("List empty")
        else:
            t=self.head
            q=t
            t=t.next
            while(t.next != None):
                t=t.next
                q=q.next
            q.next=None
            if q==self.head:
                self.head=None

    def deleteLeft(self):
        if self.head==None:
            print("List is empty")
        else:
            t=self.head               #making a copy
            self.head=self.head.next   #shifting the root node so that reference is removed
            print(f"Deleted {t.data}") 
            #deleting t

    def printList(self):
        temp=self.head
        while (temp!=None):
            print(f"| {temp.data} |->",end="")
            temp=temp.next
    
    def search(self,key):
        if self.head==None:
            print("List empty")
        else:
            temp=self.head
            count=0
            while temp!=None:
                count += 1
                if temp.data==key:
                    print(f"{temp.data} found at position {count}")
                    break
                temp=temp.next
            return print("False")
    
objlist=LinkedList()
objlist.insertRight(10)
objlist.insertRight(5)
objlist.insertRight(69)
objlist.printList()
print()
objlist.search(7)