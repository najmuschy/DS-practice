def find_target(nums, k):
    low= 0
    high = len(nums)-1

    while low<=high:
        mid = (low+high)//2
        print(f'mid {nums[mid]}')
        if nums[mid]==k:
            return mid
        if nums[low]==nums[mid]==nums[high]:
            continue
        if nums[mid]<nums[low]:
            if nums[mid]==k:
                return mid
            if k>nums[mid] and k<=nums[high]:
                low=mid+1
            else:
                high = mid-1
            
        else:
            print(f'high {high} mid{mid} low{low}')
            if nums[mid]==k:
                return mid
            if k>=nums[low] and k<nums[mid]:
                high= mid-1
            else:
                low = mid+1
    
list = [7,8,9,1,2,3,4,5,6]

print(find_target(list, 6))
