l = []
source = list(range(1,31))
result = []
for _ in range(28):
    t = int(input())
    l.append(t)
for i in range(30):
    if source[i] not in l:
        result.append(source[i])
print(min(result))
print(max(result))