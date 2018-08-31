#!/bin/python3

import sys


n = int(input().strip())
a = []
# this also serves as the length if you add one
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   a.append(float(a_t))
   a.sort()
   # if it's even length
   if (a_i % 2 == 1):
       print((float(a[a_i // 2]) +
             float(a[a_i // 2 + 1])) / 2)
   else:
       print(float(a[a_i // 2]))
