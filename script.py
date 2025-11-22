#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""List Sorter with Multiple Algorithms"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    numbers = [61,51,58,8,19,35,72,1,56,60]
    
    print(f"Original: {numbers}")
    sorted_nums = bubble_sort(numbers.copy())
    print(f"Sorted: {sorted_nums}")
