def is_matched(expression):
    close = {')':'(', '}':'{', ']':'['}
    opens = set(close.values())
    balanced = []
    for c in expression:
        if c in opens:
            balanced.append(c)
        elif c in close:
            if balanced == []:
                return False
            elif balanced[-1] == close.get(c):
                balanced.pop()
            else:
                return False
        else:
            return False
    return balanced == []    

