import sys


def subarray(nums):
    
    max= -sys.maxsize-1
    start = 0
    ansEnd = 0
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
        if sum>max:
            max = sum
            ansStart=start
            ansEnd = i
        if sum<0:
            sum = 0
            start= i+1
    if max>0:
        print(ansStart)
        print(ansEnd)
        return max
    return {}
    
list = [-2, 4, -5, 6, -7, 6, 6]
print(subarray(list))

