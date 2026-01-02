list = [10, 20, 30, 40, 50]
low = 0
high  = len(list)-1
value = 50
while low <= high:
    mid = int((low+high)/2)

    if list[mid] == value:
        index = mid
        break
    elif list[mid] < value:
        low = mid+1
    else:
        high = mid-1
print(index-1)