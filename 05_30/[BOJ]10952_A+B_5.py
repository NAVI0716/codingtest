result = []
count = 0

while True:
    a, b = map(int,input().split())
    if a != 0 and b != 0:
        result.append(a+b)
        # print(a+b)
    else:
        break
for i in result:
    print(i)