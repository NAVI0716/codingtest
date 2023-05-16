val = map(int,input().split())
result = 0
for i in val:
    result += i**2
print(result%10)