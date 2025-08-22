def permutaion(index, nums, result):
    if index ==  len(nums):
        result.append(nums.copy())
        return
    
    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        permutaion(index+1, nums, result)
        nums[index], nums[i] = nums[i], nums[index]

nums = [1,2,3]
result = []

permutaion(0, nums, result)
print(result)