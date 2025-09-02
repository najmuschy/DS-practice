from collections import deque
def convert(expression:str):
    stack = deque()

    for ch in reversed(expression):

        if ch.isalnum():
            stack.append(ch)
        else:
            t1 = stack.pop()
            t2 = stack.pop()

            t3 = f'({t1}{ch}{t2})'
            stack.append(t3)
    ans = ''.join(stack)[1:-1]
    return ans
    

expression = '*+PQ-MN'

print(convert(expression))