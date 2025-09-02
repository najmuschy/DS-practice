def singleNumber(nums):

    ans = 0
    count = 0
    for i in range(32):
        count = 0
        for num in nums:
            if num & (1<<i):
                count+=1
        if count%3==1:
            ans = ans | 1<<i
    return ans

list = [2,2,3,2]

print(singleNumber(list))