#!/bin/python3

import sys

def getWays(n, c):
    c.sort()
    max_coin = max(c)
    P = []
    for v in range(n + 1):
        P.append([0] * (max_coin + 1))
    # seeding one base case
    for mc in range(1, max_coin + 1):
        P[0][mc] = 1
    
    # d y n a m i c p r o g r a m m i n g
    for v in range(1, n + 1):
        for mc in range(1, max_coin + 1):
            for coin in c:
                if coin > mc or v - coin < 0:
                    break
                P[v][mc] += P[v - coin][coin]
    print(P)
    return P[n][max_coin]
                

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
