queue=[]
front=0
rear=-1
def enqueue():
    temp=queue.append(int(input("Enter the data: ")))
    print(f"Element pushed: {temp}")
    rear += 1

def dequeue():
    if front>rear:
        print("Stack empty")
    else:
        queue.pop()
        front += 1
    


def printQueue():
    if (front>rear):
        print("Stack is empty")
    else:
        for i in range(0,len(queue)+1):
            print(queue[i])

while True:
    print(f"1.Enqueue 2.Dequeue 3.Print 4.Exit")
    ch=int(input("Enter choice "))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        printQueue()
    elif ch==4:
        break
    else:
        print("Invalid choice")