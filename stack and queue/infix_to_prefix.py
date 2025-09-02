from collections import deque
def priority(chara):
    if chara == '^':
        return 3
    elif chara == '*' or chara=='/':
        return 2
    elif chara == '+' or chara=='-':
        return 1
    else:
        return -1
def reverseexp(expression:str):
    expression = list(expression[::-1])

    for i in range(len(expression)):
        if expression[i]=='(':
            expression[i]=')'
        elif expression[i]==')':
            expression[i]='('
    return ''.join(expression)

def convert(expression):
    ans = ''
    expression = reverseexp(expression)
    stack = deque()
    for ch in expression:

        if ch.isalnum():
            ans += ch
        else:
            if ch=='(':
                stack.append(ch)
                continue
            elif ch == ')':
 
                while stack:
                    popped = stack.pop()
                    if popped=='(':
                        break
                    ans+=popped
            else:
                if ch=='^':
                    while stack and priority(stack[len(stack)-1])<=priority(ch):
                        ans+=stack.pop()
                    stack.append(ch)
                else:
                    while stack and priority(stack[len(stack)-1])>priority(ch):
                        ans+=stack.pop()
                    stack.append(ch)


    
    while stack:
        ans+= stack.pop()
    return ans

expression = "(a+b)*c-d+f"
print(convert(expression))                

