t = int(input())
t_l= list(map(int,input().split()))
search = int(input())
count = 0 
for i in t_l:
    if i == search:
        count += 1
print(count)        