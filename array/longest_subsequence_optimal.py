def long_subsequence(nums):
    count =1
    maxCount = 1
    storage = set()

    for num in nums:
        storage.add(num)

    for num in storage:

        if num-1 not in storage :
            count=1
            while num+1 in storage:
                num=num+1
                count= count+1
        maxCount = max(count, maxCount)
    return maxCount

list = [1,0,1,2]

print(long_subsequence(list))