class Node:
    def __init__(self,data):
        self.data=data           #defining the structure of the node
        self.next=None

class QueueStack:
    def __init__(self):
        self.head=None

    def Enqueue(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
        else:
            temp=self.head
            while(temp.next != None):
                temp=temp.next
            temp.next=n
            


    def Dequeue(self):
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
    

    
objlist=QueueStack()
