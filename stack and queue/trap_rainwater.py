from collections import deque
def trap(height):
    n = len(height)
    ngeL = []
    stack = []
    max1 = -1
    max2 = -1
    for i in range(n):
        while stack and height[i] > stack[-1]:
            stack.pop()
        ngeL.append(stack[-1] if stack else -1)
        max1 =max(max1,height[i])
        stack.append(max1)


    ngeR = deque()
    stack.clear()
    for i in range(n-1, -1, -1):
        while stack and height[i] >= stack[-1]:
            stack.pop()
        ngeR.appendleft(stack[-1] if stack else -1)
        max2 = max(max2, height[i])
        stack.append(max2)
    sum = 0
    for i in range(n):

        if ngeL[i]>0 and ngeR[i]>0:
            sum+= min(ngeL[i], ngeR[i])- height[i]
    
    return sum
    

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
