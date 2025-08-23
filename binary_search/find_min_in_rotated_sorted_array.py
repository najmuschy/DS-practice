#find min
import sys
def find_min(nums):
    minn = sys.maxsize

    low= 0
    high = len(nums)-1
    index = -1
    while low<=high:

        mid = (low+high)//2

        if nums[mid]<nums[low]:
            if nums[mid]<minn:
                minn = nums[mid]
                index = mid
            high = mid-1
        else:
            if nums[low]<=minn:
                minn = nums[low]
                index = low
            low = mid+1
    
    return minn

list =[4,5,6,7,9,1,2,3]
print(find_min(list))