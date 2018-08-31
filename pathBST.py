""" 
Reference BST
  
       17       
     /    \ 
   6       46
 /   \       \
 3   12       56
/   /  \     /
1   9  15   48 
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def lookup(self, data):
        lst = [self]
        if data == self.data:
            return lst
        if data > self.data and self.right:
            lst.extend(self.right.lookup(data))
            return lst
        if data < self.data and self.left:
            lst.extend(self.left.lookup(data))
            return lst
        return []

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return self.data

def pathBST(head, d1, d2):
    path1 = head.lookup(d1)
    path2 = head.lookup(d2)
    s = set(path1)
    common = None
    for val in path2[::-1]:
        if val in s:
            common = val
            break
    if not common:
        print("Something bad happened!")
        return
    p1 = common.lookup(d1)
    p2 = common.lookup(d2)
    return p1[::-1] + p2[1:]
    

# construction
head = Node(17)
head.left = Node(6)
curr = head.left
curr.left = Node(3)
curr.left.left = Node(1)
curr.right = Node(12)
curr.right.left = Node(9)
curr.right.right = Node(15)

head.right = Node(46)
curr = head.right
curr.right = Node(56)
curr.right.left = Node(48)

print(head.lookup(15))
