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

def ransom_note(magazine, ransom):
    ransom_d = {}
    mag_d = {}
    for word in ransom:
        ransom_d[word] = ransom_d.get(word, 0) + 1
        
    for word in magazine:
        mag_d[word] = mag_d.get(word, 0) + 1
        
    for key in ransom_d:
        if mag_d.get(key):
            if ransom_d[key] > mag_d[key]:
                return False
        else:
            return False
    return True

def array_left_rotation(a, n, k):
    lst1 = a[:k]
    lst2 = a[k:]
    return lst2 + lst1

def has_cycle(head):
    seen = set()
    current = head
    while current:
        if current in seen:
            return True
        
        seen.add(current)
        current = current.next
        
    return False

def checkBST(root):
    return check(root, 0, 10000)

def check(root, min, max):
    if root is None:
        return True
    if root.data >= max or root.data <= min:
        return False
    return check(root.left, min, root.data) and check(root.right, root.data, max)
  
  