class Solution(object):
    def numJewelsInStones(self, J: str, S: str) -> None:
        jewelSet = set()
        for jewel in J:
            jewelSet.add(jewel)

        count = 0
        for stone in S:
            if stone in jewelSet:
                count += 1
        return(count)
        
J = "aA"
S = "aAAbbbb"
s = Solution()
print(s.numJewelsInStones(J, S))