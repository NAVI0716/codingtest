result = []
while True:
    x,y = map(int,input().split())
    if x > y:
        result.append("Yes")
    elif x == 0 and y == 0:
        for i in result:
            print(i)
        break
    else:
        result.append("No")
