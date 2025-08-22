import math
def majority_el(nums):
    i=0
    count =0
    el=nums[i]

    while i<len(nums):
        if el == nums[i]:
            count +=1
            i=i+1
        elif el!= nums[i]:
            count-=1
            i+=1
            if i==len(nums):
                break
            if count==0:
                el= nums[i]
    
    if count>0:
        temp_count = 0
        for i in nums:
            if i==el:
                temp_count+=1
        if temp_count>(len(nums)/2):
            return el
    return 0

list = [7,7,7,5,5,5,5,3,7,7,7]

print(majority_el(list))




