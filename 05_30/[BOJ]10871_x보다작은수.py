A, B = map(int,input().split())
t_l = list(map(int,input().split()))
result = []
for i in t_l:
    if i < B:
        result.append(i)
print(*[i for i in result])
