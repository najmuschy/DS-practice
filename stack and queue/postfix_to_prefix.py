from collections import deque
def convert(expression:str):
    stack = deque()

    for ch in expression:

        if ch.isalnum():
            stack.append(ch)
        else:
            t1 = stack.pop()
            t2 = stack.pop()

            t3 = f'{ch}{t2}{t1}'
            stack.append(t3)
    ans = ''.join(stack)
    return ans
    
expression = 'AB-DE+F*\\'

print(convert(expression))