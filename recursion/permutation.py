from collections import defaultdict
def permuation(ds:list, nums:list, result:list[list], freq:dict):

    if len(ds)==len(nums):
        result.append(ds.copy())
        return
    for num in nums:
        if num not in freq:
            freq[num]=1
            ds.append(num)
            permuation(ds, nums, result, freq )
            del freq[num]
            ds.pop()

nums = [1,2,3]
result = []
freq = defaultdict(int)
ds=[]

permuation(ds, nums, result, freq)

print(result)