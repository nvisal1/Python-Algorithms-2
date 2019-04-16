"""
Name: Nicholas Visalli 
Assignment number: 2
Purpose: Generate a binary search tree and determine the average depth
"""

from random import *

class Node: 
    """Constructor for Node class
    """
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

    """Determine depth of given node
    :param self: Node to determine depth of
    :type self: Node
    :returns: None 
:   rtype: None
    """
    def depth(self):
        return max(self.left.depth() if self.left else 0, self.right.depth() if self.right else 0) + 1

"""Insert a node into the binary search tree
:param root: root node of binary search tree
:type root: Node
:param node: node to insert into binary search tree
:type node: Node
:returns: None 
:rtype: None
"""
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

"""Print binary search tree nodes inorder
:param root: root node of binary search tree
:type root: Node
:returns: None 
:rtype: None
"""
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 


r = Node(randint(0, 50000)) 
depth = 0
for i in range(4999):
    insert(r, Node(randint(0, 50000)))
    depth = depth + r.depth();


inorder(r)
print('avg depth: ', depth/5000)