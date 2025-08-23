
def find_unique_element(nums):

    low = 1
    high = len(nums)-2

    if len(nums)==1:
        return nums[1]
    if nums[low-1]!=nums[low]:
        return nums[low-1]
    if nums[high+1]!=nums[high]:
        return nums[high+1]
    
    while low<=high:

        mid = (low+high)//2

        if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
            return nums[mid]
        
        if mid%2==0:

            if nums[mid]!=nums[mid-1]:
                low= mid+1
            else:
                high = mid-1
        else:
            if nums[mid]!=nums[mid-1]:
                high=mid-1
            else:
                low = mid+1

        
list = [1,1,2,2,3,4,4,5,5,6,6]

print(find_unique_element(list))