base_source = (1, 1, 2, 2, 2, 8)
t_ls = [i for i in map(int,input().split()) ]
result = []
for i in range(len(base_source)):
    if t_ls[i] == base_source[i]:
        result.append(0)
    else:
        result.append(-t_ls[i]+base_source[i])
print(*result)
