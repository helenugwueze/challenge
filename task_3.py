def balance_brackets(text):
    stack = []
    pairs = {')':'(',']':'[','}':'{'}
    for c in text:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if not stack or stack[-1] != pairs[c]:
                return false
            stack.pop()
    return len(stack) == 0

cal = balance_brackets(["(hello)"]) 
print(cal)                   