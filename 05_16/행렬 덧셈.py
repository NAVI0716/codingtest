#case1
x,y = map(int,input().split())
A=[]
B=[]
result=[]
for _ in range(2):
    if len(A) != 3:
        for i in range(x):
            A.append(list(map(int,input().split())))      
    else:
        for i in range(x):
            B.append(list(map(int,input().split())))

lam = lambda x,y:x+y
for i in range(x):
    l=[]
    for j in range(y):
        l.append(lam(A[i][j],B[i][j]))
    result.append(l)
for i in result:
    print(*i)

#case2
a,b = map(int,input().split())
count=0
A=[]
B=[]
for i in range(2*a):
    count+=1
    if count<4:
        z,x,c=map(int,input().split())
        A.append([z,x,c])
    elif count >3 and count <7:
        z,x,c=map(int,input().split())
        B.append([z,x,c])
    else:
        break

result = []
for i in range(a):
    temp=[]
    for j in range(b):
        temp.append(A[i][j]+B[i][j])
    result.append(temp)
for i in result:
    print(*i)

#case 3
a,b = map(int,input().split())
count=0
A=[]
B=[]
for i in range(a):
            A.append(list(map(int,input().split())))   
for i in range(x):
            B.append(list(map(int,input().split())))   

for i in range(a):
    for j in range(b):
        print(A[i][j]+B[i][j],end= " ")
    print()