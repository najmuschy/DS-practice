
def subsets(nums):
    subsets = 2**len(nums)
    ans = []
    for i in range(subsets):
        list = []
        for j in range(len(nums)):
            if i & (1<<j):
                list.append(nums[j])
        ans.append(list)
    return ans

list = [1,2,3]

print(subsets(list))

