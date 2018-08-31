#!/bin/python3

import sys

def getWays(n, c):
    c.sort()
    max_coin = max(c)
    P = []
    for v in range(n + 1):
        P.append([0] * (len(c)))
    # seeding one base case
    for coin_index in range(len(c)):
        P[0][coin_index] = 1
    
    # d y n a m i c p r o g r a m m i n g
    for v in range(1, n + 1):
        for i, max_coin in enumerate(c):
            for j in range(i + 1):
                coin = c[j]
                if v - coin < 0:
                    break
                P[v][i] += P[v - coin][j]
    return P[n][-1]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
