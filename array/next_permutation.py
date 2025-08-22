
def next_permutation(nums):
    index = -1
    for i in range(len(nums)-2, -1, -1):
        if nums[i]<nums[i+1]:
            index = i
            break
    

    if index==-1:
        nums[:] = nums[::-1]
    

    else:
        for i in range(len(nums)-1, index, -1):
            # print(nums[i])
            if nums[i]>nums[index]:
                nums[index], nums[i] = nums[i], nums[index]
                break
        nums[index+1:] = nums[index+1:][::-1]

list = [1,4,3,2]

next_permutation(list)
print(list)
        