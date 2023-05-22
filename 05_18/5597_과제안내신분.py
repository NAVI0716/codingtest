l = []
source = [range(1,31)]
result = []
for _ in range(27):
    t = int(input())
    l.append(t)
for i in range(28):
    if l[i] not in source:
        result.append(l[i])
print(min(result))
print(max(result))
