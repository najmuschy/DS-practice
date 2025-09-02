def near(nums):
    n=len(nums)
    result = [-1]*len(nums)
    list = []
    for i in range(n):
        
        while  list and list[-1]>nums[i]:
            list.pop()
        if list:
            result[i]= list[-1]
        list.append(nums[i])
    return result

print(near([4,5,2,10,8]))