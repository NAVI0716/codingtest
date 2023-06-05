def FAT(t):
    if t > 1:
        return t * FAT(t-1)
    else:
        return 1

t = int(input())
print(FAT(t))