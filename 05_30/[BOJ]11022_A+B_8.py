result = {}
c=0
t = int(input())
for i in range(t):
    c+=1
    a,b = map(int,input().split())
    result[c] = (a,b,a+b)
for a,b in result.items():
    print(f"Case #{a}: {b[0]} + {b[1]} = {b[2]}")
