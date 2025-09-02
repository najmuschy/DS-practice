def minDays(bloomDay, m, k):

    if len(bloomDay)<m*k:
        return -1
    max = bloomDay[0]
    min = bloomDay[0]
    for bloom in bloomDay:
        if bloom>max:
            max=bloom
        if bloom<min:
            min=bloom

    low = min
    high = max

    while low<=high:

        mid = (low+high)//2
        bouque=0
        count=0
        for bloom in bloomDay:
            if bloom<=mid:
                count+=1
            else:
                bouque+= count//k
                count = 0
        
        bouque+=count//k
        print(f'mid {mid} boque {bouque}')

        if bouque>=m:
            high = mid-1
        else:
            low = mid+1
    if low>max:
        return -1
    return low

list = [7,7,7,8,12,7,7,7]

print(minDays(list, 2,2))
                
        