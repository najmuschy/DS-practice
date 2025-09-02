from collections import deque
def priority(chara):
    if chara == '^':
        return 3
    elif chara == '*' or '/':
        return 2
    elif chara == '+' or '-':
        return 1
    else:
        return -1
    
def convert(expression):
    stack = deque()
    ans = ''
    for ch in expression:
        if ch.isalnum():
            ans+=ch
        else:
            if not stack:
                stack.append(ch)
            elif ch=='(':
                stack.append(ch)
            elif ch==')':
                 while stack:
                    ch = stack.pop()
                    if ch=='(':
                         break
                    ans+=ch
            elif priority(ch)<=priority(stack[len(stack)-1]):
                while (len(stack)!=0 and priority(ch)<=priority(stack[len(stack)-1])):
                    ans+= stack.pop()
                
                stack.append(ch)
            else:
                stack.append(ch)
    
    if len(stack):
        while len(stack):
            ans+= stack.pop()

    return ans

expression = 'a+b*(c^d-e)'
print(convert(expression))