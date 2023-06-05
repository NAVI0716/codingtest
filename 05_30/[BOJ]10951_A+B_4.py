result = []
count = 0

while True:
    try:
        a, b = map(int,input().split())
        result.append(a+b)
        # print(a+b)
    except:
        break
for i in result:
    print(i)