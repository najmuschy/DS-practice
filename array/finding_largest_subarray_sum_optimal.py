
def subarray_list(list1,k):
    left = 0
    right = 0
    maxlen = 0
    sum= 0
    while right< len(list1):
        if right< len(list1): sum+=list[right]

        while left<=right and sum>k:
            sum = sum-list[left]
            left+=1
        if sum==k:
            maxlen = max(maxlen, right-left+1)
            
        
        # print(f'right {right}, sum {sum} list[right]-->{list[right]}')
        right+=1

    return maxlen 

list = [1,2,1,1,0,3]

result = subarray_list(list,3)

print(result)
