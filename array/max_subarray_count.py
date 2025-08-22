from collections import defaultdict
def max_subarray_count(nums,k):
    sums = defaultdict(int)
    sum = 0
    count = 0
    sums[0]=1
    for num in nums:

        sum= sum + num
        rem = sum - k
        if rem in sums:
            count += sums[rem]
        
        sums[sum]+=1
       
    return count
    
nums = [0,0,0,0,0,0,0,0,0,0] 
count = max_subarray_count(nums,0)
print(count)

        

