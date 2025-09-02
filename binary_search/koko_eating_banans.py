
def min_eating_speed(piles, h):

    max = piles[0]
    
    for pile in piles[1:]:
        if pile>max:
            max = pile
    
    low =1
    high = max

    while low<=high:

        mid = (low+high)//2
        totalHours = 0
        
        for pile in piles:
            totalHours+= -(-pile//mid)

        if totalHours<=h:
            high = mid-1
        else :
            low = mid+1
    return low

bananas = [30,11,23,4,20]
print(min_eating_speed(bananas, 5))
