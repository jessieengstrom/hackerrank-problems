def is_matched(expression):
    """Checks if all brackets are matching."""
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
    """Checks if all words in ransom note are in magazine."""
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
    """Rotates an array left by k."""
    lst1 = a[:k]
    lst2 = a[k:]
    return lst2 + lst1

def has_cycle(head):
    """Does the linked list have a cycle."""
    seen = set()
    current = head
    while current:
        if current in seen:
            return True
        
        seen.add(current)
        current = current.next
        
    return False

def checkBST(root):
    """Is this a binary search tree."""
    return check(root, 0, 10000)

def check(root, min, max):
    """Is this a binary search tree."""
    if root is None:
        return True
    if root.data >= max or root.data <= min:
        return False
    return check(root.left, min, root.data) and check(root.right, root.data, max)
  
def print_list(head):
    """Print all contents of a linked list."""
    if head is None:
        pass

    while head:
        print head.data
        head = head.next


"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    """Insert data at the end of a linked list."""
    new = Node(data)
    if head is None:
        head = new
        return head
    current = head
    while current.next:
        current = current.next
        
    current.next = new
    return head


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def preOrder(root):
    """Pre-order tree traversal."""
    if root:
        print root.data,
        preOrder(root.left) 
        preOrder(root.right) 

"""
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
"""

def height(root):
    """Get the height of the tree."""
    if not root:
        return -1
    height_left = 1 + height(root.left)
    height_right = 1 + height(root.right)
    
    return max(height_left, height_right)


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
   """Print tree nodes in level order."""
    to_visit = [root]
    seen = []
    
    while to_visit:
        current = to_visit.pop(0)
        seen.append(current.data)
        
        if current.left != None and current.right != None:
            to_visit.extend([current.left, current.right])
        elif current.left != None:
            to_visit.append(current.left)
        elif current.right != None:
            to_visit.append(current.right)
        else:
            continue
        
    for item in seen:
        print item,


def insert(r,val):
   """Insert a node into a binary search tree."""
    if r is None:
        r = Node(val)
    elif val < r.data:
        if r.left is None:
            r.left = Node(val)
        else:
            insert(r.left, val)        
    elif val > r:
        if r.right is None:
            r.right = Node(val)
        else:
            insert(r.right, val)
            
    return r

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if not headA or not headB:
        head = headA or headB
        return head
    elif headA.data < headB.data:
        smaller = headA
        smaller.next = MergeLists(headA.next, headB)    
    else:
        smaller = headB
        smaller.next = MergeLists(headA, headB.next)
        
    return smaller
  