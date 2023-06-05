n, m, t_num = map(int,input().split())
c = -1
# for i in range(n):
#     for j in range(m):
#         c+=1
#         if c == t_num:
#             print(f"{i} {j}")
#             break
print(f'{t_num//m} {t_num%m}')
