result = []
c=0
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    result.append(a+b)
for i in result:
    c+=1
    print(f"Case #{c}: {i}")
