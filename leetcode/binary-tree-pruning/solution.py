"""Approach
So we're going to want a recursive solution

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, node: TreeNode) -> TreeNode:
        if not node:
            return node
        
        self.pruneTree(node.left)
        self.pruneTree(node.right)
        
        pruneLeft = self.canPrune(node.left)
        pruneRight = self.canPrune(node.right)
        if pruneLeft:
            node.left = None
        if pruneRight:
            node.right = None

        if node.val == 0 and pruneLeft and pruneRight:
            return None
        return node

        
    def canPrune(self, node: TreeNode) -> bool:
        if not node:
            return True
        return node.val == 0 and self.canPrune(node.left) and self.canPrune(node.right)