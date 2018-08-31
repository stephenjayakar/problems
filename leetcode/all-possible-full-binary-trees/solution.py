""" 
I actually really enjoyed this problem, though struggled quite a bit
at the start.  I didn't really realize it was dynamic programming
until I started implementing a dynamic programming algorithm.  Maybe
get better at expressing the ideas out before actually trying to code
them; it will be easier for recruiters to understand what you're doing then.
"""

"""
Solutions:
3: [0, 0, 0]
"""
class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # This solution doesn't copy trees, so not memory safe on tree-write
    # could be fixed by copying the tree by hand :) 
    def allPossibleFBT(self, N: int) -> list:
        # Create Tree Node
        def ctn():
            return TreeNode(0)
        # N = 3
        def baseTree():
            tn = ctn()
            tn.left = ctn()
            tn.right = ctn()
            return tn
        # if even, DNE
        if not (N % 2):
            return []
        if N == 1:
            return [ctn()]
        if N == 3:
            return [baseTree()]

        part_solns = [[ctn()], [baseTree()]]
        for i in range(5, N + 1, 2):
            soln = []
            for left in range(1, i, 2):
                right = i - left - 1
                for left_sol in part_solns[(left - 1) // 2]:
                    for right_sol in part_solns[(right - 1) // 2]:
                        tn = ctn()
                        tn.left = left_sol
                        tn.right = right_sol
                        soln.append(tn)
            part_solns.append(soln)
        return part_solns[-1]

s = Solution()
x = s.allPossibleFBT(7)
print(x)
