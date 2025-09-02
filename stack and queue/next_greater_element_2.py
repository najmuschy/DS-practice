from collections import deque
def next_greater(nums):
    n= len(nums)
    stack = deque()
    result = [-1]* n

    for i in range((2*n)-1, -1,-1):

        if i>n-1:
            while stack and nums[i%n]>stack[-1]:
                stack.pop()

            stack.append(nums[i%n])
        else:
            while stack and nums[i]>=stack[-1]:
                stack.pop()

            if stack:
                result[i]=stack[-1]
            stack.append(nums[i])
        
    return result

print(next_greater([1,7,2,6]))

