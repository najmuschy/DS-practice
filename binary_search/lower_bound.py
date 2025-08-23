import math
def lower_bound(nums, target):
    low = 0
    high = len(nums)-1
    ans = len(nums)
    while low<=high:

        mid = math.floor((low+high)/2)
        if nums[mid]>=target:
            ans = mid
            high= mid-1
        elif nums[mid]<target:
            low=mid+1
    return ans

list = [1,2,3,4,5,8,8,9,10,10,11]


print(lower_bound(list, 9))