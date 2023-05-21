def alnum(line):
    if line.isalnum()==True:
        print("True")
    else:
        pass
def alpha(line):
    if line.isalpha()==True:
        print("True")
    else:
        pass
def digit(line):
    if line.isdigit()==True:
        print("True")
    else:
        pass
def lower(line):
    if line.islower()==True:
        print("True")
    else:
        pass
def upper(line):
    if line.isupper()==True:
        print("True")
    else:
        pass

string1=input()
charlist=[]
for i in range(len(string1)):
    charlist.append(string1[i])
print(charlist)









