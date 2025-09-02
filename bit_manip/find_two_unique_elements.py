def singleNumber(nums):

    b1= 0
    b2 = 0
    xor = 0

    for num in nums:
        xor = xor ^ num
    
    last_bit = (xor &(xor-1) ) ^ xor

    for num in nums:
        if num & last_bit ==0:
            b1 = b1^num
        else:
            b2 = b2^num
    return [b2,b1]

nums = [1,2,1,3,2,5]
print(singleNumber(nums))