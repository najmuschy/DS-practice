

def sort012(list):

    low = 0
    mid = 0
    high = len(list)-1

    while mid<=high:

        if list[mid]==0:
            list[low],list[mid] = list[mid],list[low]
            mid=mid+1
            low=low+1
        elif list[mid]==1:
            mid=mid+1
        else:
            list[mid], list[high] = list[high], list[mid]
            high= high-1

    
list  = [0,1,2,1,1,0,2,1,1,0,2]

sort012(list)

print(list)