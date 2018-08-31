class Solution:
    def matrixScore(self, A: list) -> int:
        rows = len(A)
        cols = len(A[0])

        def rowToBinVal(row):
            return sum([x << i for i, x in enumerate(reversed(row))])

        def flipRow(A, r: int):
            row = A[r]
            for i in range(len(row)):
                row[i] = 1 - row[i]

        def flipCol(A, c: int):
            for r in range(len(A)):
                row = A[r]
                row[c] = 1 - row[c]

        # first phase, get all 1s in the left column
        for r in range(rows):
            row = A[r]
            # if the first value is a 0
            if not row[0]:
                flipRow(A, r)

        for c in range(cols):
            # check how many 1s in each col, flip if 
            ones = 0
            for r in range(rows):
                if (A[r][c]):
                    ones += 1
            if ones <= rows / 2:
                flipCol(A, c)

        returnVal = 0
        for row in A:
            returnVal += rowToBinVal(row)
        return returnVal
      

S = Solution()            
A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(S.matrixScore(A))