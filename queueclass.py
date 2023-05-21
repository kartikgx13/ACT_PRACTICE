class CreateQueue:
    queue=[]
    front=0
    rear=-1
    def enqueue(self):
        temp=0
        temp=self.queue.append(int(input("Enter the data: ")))
        print(f"Element pushed: {temp}")
        self.rear += 1

    def dequeue(self):
        if self.front>self.rear:
            print("Stack empty")
        else:
            self.queue.pop(0)
        self.front += 1
    


    def printQueue(self):
        if (self.front>self.rear):
            print("Stack is empty")
        else:
            for i in range(0,len(self.queue)):
                print(self.queue[i])

queueobj=CreateQueue()

while True:
    print(f"1.Enqueue 2.Dequeue 3.Print 4.Exit")
    ch=int(input("Enter choice "))
    if ch==1:
        queueobj.enqueue()       
    elif ch==2:
        queueobj.dequeue()
    elif ch==3:
        queueobj.printQueue()
    elif ch==4:
        break
    else:
        print("Invalid choice")