class CreateQueue:
    queue=[]
    front=0
    rear=-1
    maxSize=0
    count=0
    def enterSize(self,maxSize):
        self.maxSize=maxSize                               
    
    def printQueue(self):
        if (self.count==0):
            print("Queue is empty")
        else:
            for i in range(0,len(self.queue)):
                print(self.queue[i],end="-->")
    
    def enqueue(self):
        if (self.count==self.maxSize):
            print("Queue is full")
        else:
            self.queue.append(int(input("Enter data: ")))
            self.count += 1
            self.rear=(self.rear+1)%self.maxSize
    
    def dequeue(self):
        if (self.count==0):
            print("Queue is empty")
        else:
            self.queue.pop(0)
            self.count -= 1
            self.front=(self.front+1)%self.maxSize

objqueue=CreateQueue()
size=int(input("Enter max size"))
objqueue.enterSize(size)

while True:
    print(f"1.Enqueue 2.Dequeue 3.Print 4.Exit")
    ch=float(input("Enter your choice: "))
    if ch==1:
        objqueue.enqueue()
    elif ch==2:
        objqueue.dequeue()
    elif ch==3:
        objqueue.printQueue()
    elif ch==4:
        break
    else:
        print("Invalid choice")