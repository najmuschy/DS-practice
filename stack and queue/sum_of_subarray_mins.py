from collections import deque
def sum(arr):
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
    
    nse = findnse(arr)
    psee = findpsee(arr)
    totalmin = 0
    for i in range(len(arr)):

        left = i - psee[i]
        right  = nse[i]-i
        total+=(left*right*arr[i]%modulo)%modulo
    return total 

print(sum([11,81,94,43,3]))
            




