from collections import deque
def sum(nums):
    modulo = 10**9 + 7
    def findnse(arr):
        ans = deque()
        stack =deque()
        

        for i in range(len(arr)-1, -1, -1):

            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            
            ans.appendleft(stack[-1] if stack else len(arr))

            stack.append(i)
        
        return ans
    
    def findpsee(arr):
        ans = []
        stack = deque()

        for i in range(len(arr)):
            while stack and arr[stack[-1]]> arr[i]:
                stack.pop()
            
            ans.append(stack[-1] if stack else -1)
            stack.append(i)

        return ans
    def findnge(arr):
        ans = deque()
        stack = deque()
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            
            ans.appendleft(stack[-1] if stack else -1)
            stack.append(i)
        return ans
    def findpge(arr):
        ans = []
        stack = deque()
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            
            ans.append(stack[-1] if stack else -1)
            stack.append(i)
        return ans



    nse = findnse(nums)
    psee = findpsee(nums)
    pge = findpge(nums)
    nge = findnge(nums)

    totalmin = 0
    totalmax = 0
    for i in range(len(nums)):

        leftmin = i - psee[i]
        rightmin  = nse[i]-i
        leftmax = i-pge[i]
        rightmax = (nge[i] if nge[i]!=-1 else len(nums))-i


        totalmax =( totalmax + (rightmax*leftmax*nums[i]))
        totalmin =(totalmin + (leftmin*rightmin*nums[i]))
        print(totalmin)
    return totalmax-totalmin

print(sum([4,-2,-3,4,1]))
            




