from collections import deque
def next_greater_element(nums1, nums2):
    n= len(nums2)
    stack = deque()
    final_result = [-1]*n
    for i in range(n-1, -1, -1):

        while stack and stack[-1]<nums2[i]:
            stack.pop()
        if stack:
            final_result[i]= stack[-1]
        
        stack.append(nums2[i])
    nums2_index = {val:idx for idx,val in enumerate(nums2)}
    result = []

    for num in nums1:
        index = nums2_index[num]
        result.append(final_result[index])


    return result    



print(next_greater_element([2,1,3], [2,3,1]))
    
