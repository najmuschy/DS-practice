import sys
def longest_subsequence(nums):
    nums.sort()
    
    count = 1
    lastSmallest = nums[0]
    maxCount = 1

    for i in range(1, len(nums)):

        if nums[i]==lastSmallest+1:
            count+=1
            lastSmallest = nums[i]
            print(lastSmallest)
        elif nums[i]==lastSmallest:
            continue
        elif nums[i]!=lastSmallest+1:
            count=1
            lastSmallest=nums[i]

        maxCount = max(maxCount, count)

    return maxCount

list = [1,0,1,2]

print(longest_subsequence(list))
    