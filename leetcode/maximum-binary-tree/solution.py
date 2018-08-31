""" Maximum Binary Tree
Problem approach: 
- Signature will have beginning and end indexes as inputs
- Find max of this range
- Recursively call with the max as the current node, and the left and right being subcalls?

EX: [3, 2, 1, 6, 0, 5]
- Insert 6 on head, call recursively on (0, 3) and (4, 6)
"""
class TreeNode:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val

    @property
    def val(self):
        return val

class Solution:
    def constructMaximumBinaryTree(self, nums):
        return Solution.helper(nums, 0, len(nums))

    def helper(nums, start: int, end: int) -> "TreeNode":
        # Base Cases
        if (end - start <= 0):
            return None
        elif (end == start + 1):
            return TreeNode(nums[start])

        # finding max value in range of values
        maxIndex = start
        maxVal = -float("inf")
        for index in range(start, end):
            if nums[index] > maxVal:
                maxIndex = index
                maxVal = nums[index]

        node = TreeNode(maxVal)
        node.left = helper(nums, start, maxIndex)
        node.right = helper(nums, maxIndex + 1, end)
        return node
