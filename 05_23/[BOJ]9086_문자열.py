t = int(input())
result = []
for i in range(t):
    tt = input()
    tt_len = len(tt)
    if tt_len >1:
        result.append(tt[0]+tt[tt_len-1])
    else:
        result.append(tt[0]+tt[0])
print(*[i for i in result], sep='\n')