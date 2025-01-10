from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        # Step 1: Check if the length is at least 3
        if n < 3:
            return False
        
        # Step 2: Find the peak
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        
        # If the peak is the first or last element, it's not a mountain
        if i == 0 or i == n - 1:
            return False
        
        # Step 3: Check if the array strictly decreases after the peak
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        # If we have reached the end, it's a valid mountain array
        return i == n - 1
