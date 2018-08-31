#!/bin/python3

import sys

# underlying structure is 1-indexed
class Heap:
    data = None
    
    def __init__(self):
        self.data = [None]

    def insert(self, val: int) -> None:
        self.data.append(val)
        
        
    def median(self) -> float:
        n = len(self.data)
        # if it's even
        if (n % 2 == 0):
            return ((float(self.data[n // 2 - 1]) +
                     float(self.data[n // 2])) / 2)
        else:
            return float(self.data[n // 2])

    def _swap(self, i: int, j: int) -> None:
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp

    # returns parent index
    def _parent(self, index: int) -> int:
        return index * 2;
        
    # returns left child index
    def _child(self. index: int) -> int:
        return index // 2

    # TODO
    def __str__(self) -> str:
        string = ""
        return str(data);
        # power of 2
        # e = 1
        # for 
        

n = int(input().strip())
a = Heap()
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   a.insert(a_t)
   # if it's even length
   print(a.median())
