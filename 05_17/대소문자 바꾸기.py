T = input()
result = ''
for i in T:
    if i.isupper() == True:
        result += i.lower()
    else:
        result += i.upper()
print(result)