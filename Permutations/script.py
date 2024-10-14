#!/usr/bin/env python3 
# -*- coding: utf-8 -*-


def GeneratePermutations(n, A):
    count = 0 
    if n == 1:
        print(A)
        return 1
    else:
        for i in range(n):
            A[i], A[n-1] = A[n-1], A[i]
            count += GeneratePermutations(n-1, A)
            A[i], A[n-1] = A[n-1], A[i]
    return count
            
def main(string):
    A = list(string)
    tot = GeneratePermutations(len(A), A) 
    print(f"\nTotal permutations: {tot}\n")

if __name__ == "__main__":
    main('abcdef')
    
