def sqroot(n):
    low =1 
    high = n

    while low<=high:
        mid = (low+high)//2
        print(f'low {low}, mid{mid}, high{high}')
        if mid*mid>n:    
            high = mid-1
        else:
            low = mid+1

    return high


print(sqroot(28))