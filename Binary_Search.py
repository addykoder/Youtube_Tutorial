
list = list(range(100))

def bin(list, n):
    l = 0
    u = len(list) - 1
    i = (u+l)//2
    while u>=l:
        if list[i] == n:
            return i
        elif list[i] > n:
            u = i-1
            i = (u+l)//2
            continue
        elif list[i] < n:
            l = i+1
            i = (u + l) // 2
            continue
    return False

print(bin(list, 130))


