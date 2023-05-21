stack=[]
def push():
    temp=stack.append(int(input("Enter the data: ")))
    print(f"Element pushed: {temp}")

def popelement():
    if len(stack)==0:
        print("Stack empty")
    else:
        stack.pop()

def peek():
    if len(stack)==0:
        print(0)
    else:
        print(stack[-1])

def printStack():
    if (len(stack)==0):
        print("Stack is empty")
    else:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])

while True:
    print(f"1.Push 2.Pop 3.Peek 4.Print 5.Exit")
    ch=int(input("Enter choice "))
    if ch==1:
        push()
    elif ch==2:
        popelement()
    elif ch==3:
        peek()
    elif ch==4:
        printStack()
    elif ch==5:
        break
    else:
        print("Invalid choice")





    



