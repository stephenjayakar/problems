"""
- Generate the left and top view of the skyline
- Iterate through the values, and add to the count min(left[row], top[col])

Input: O(N^2)
Runtime: O(N^2)
Space: O(N)
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list) -> int:
        N = len(grid)
        # generate skyline view
        left = []
        top = []
        for row in grid:
            left.append(max(row))

        for i in range(N):
            maxVal = -float("inf")
            for j in range(N):
                val = grid[j][i]
                if val > maxVal:
                    maxVal = val
            top.append(maxVal)

        count = 0
        for i in range(N):
            for j in range(N):
                val = grid[j][i]
                count += (min(left[j], top[i]) - val)
        return count

                
sol = Solution()
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(sol.maxIncreaseKeepingSkyline(grid))