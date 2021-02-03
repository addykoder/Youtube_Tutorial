def bin(list, val, l, u):
    if list[(l+u)//2] == val:
        return (l+u)//2
    elif l>u:
        return -1
    elif list[(l+u)//2] > val:
        return bin(list, val, l, ((l+u)//2)-1)
    elif list[(l+u)//2] < val:
        return bin(list, val, ((l+u)//2)+1,u)

my_list = [2,3,7,9,12,23,34,54,66,68,78,79,80,90]
print(bin(my_list, 35, 0, len(my_list)-1))
