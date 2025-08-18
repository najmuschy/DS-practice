
def subarray_sum(list, k):
    prefixSum = dict()
    sum=0
    len=0
    newLen = 0
    total = 0
    for idx, number in enumerate(list):

        sum = sum+number
        if(sum==k):
            len = idx+1
            total  +=1
        rem = sum -k 
        if rem in prefixSum:
            newLen =( idx - prefixSum[rem])
            total+=1
        if sum not in prefixSum:
            prefixSum[sum] = idx
        if newLen>len:
            len = newLen
    return total

list = [1,2,1,1,1,3,5,9,0,1,1,1]

result = subarray_sum(list,3)

print(result)
