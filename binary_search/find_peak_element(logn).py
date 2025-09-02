def find_peak(nums):

    low = 1
    high = len(nums)-2

    if len(nums)==1:
        return nums[0]
    if nums[low-1]>nums[low]:
        return 0
    if nums[high+1]>nums[high]:
        return high+1
    while low<=high:

        mid = (low+high)//2
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid
        elif nums[mid]>nums[mid-1]:
            low=mid+1
        elif nums[mid]<nums[mid-1]:
            high = mid-1
        else:
            low=mid+1
    
list = []
print(find_peak(list))