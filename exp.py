
def subarraySum( nums:list, k: int) -> int:
    prefixSum = dict()
    sum=0
    len=0
    total = 0
    newLen = 0
    for idx, number in enumerate(nums):
        sum = sum+number
        if(sum==k):
            len = idx+1
            total+=1
        rem = sum -k 
        if rem in prefixSum:
            newLen = idx-prefixSum[rem]
            total+=1
        if sum not in prefixSum:
            prefixSum[rem] = idx
        if newLen>len:
            len = newLen            
    return total
    


list = [1,2,3]

result = subarraySum(list,3)

print(result)
