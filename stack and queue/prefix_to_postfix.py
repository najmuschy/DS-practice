from collections import deque
def convert(expression:str):
    stack = deque()

    for ch in reversed(expression):

        if ch.isalnum():
            stack.append(ch)
        else:
            t1 = stack.pop()
            t2 = stack.pop()

            t3 = f'{t1}{t2}{ch}'
            stack.append(t3)
    ans = ''.join(stack)
    return ans
    
expression = '/-AB*+DEF'

print(convert(expression))