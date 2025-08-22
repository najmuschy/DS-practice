def rearrangeArray(nums):  
    posi = []
    negi = []
    posiT = 0
    negiT = 0
    for num in nums:
        if num>0:
            posi.append(num)
        else:
            negi.append(num)

    for i in range(min(len(posi),len(negi))):
        nums[i*2] = posi[i]
        nums[i*2+1]= negi[i]
        print(nums[i*2+1])
        posiT+=1
        negiT+=1

    while posiT<len(posi) or negiT<len(negi):
        print(1)
        if posiT<len(posi):
            nums.append(posi[posiT])
            posiT+=1
        if negiT<len(negi):
            nums.append(negi[negiT])
            negiT+=1
    return nums

list = [3,1,2,-5,2,-4]
rearrangeArray(list)
print(list)