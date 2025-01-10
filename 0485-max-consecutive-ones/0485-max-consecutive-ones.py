from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  # Variable to store the maximum streak of consecutive 1's
        current_count = 0  # Variable to store the current streak of consecutive 1's
        
        # Iterate through the array
        for num in nums:
            if num == 1:
                current_count += 1  # Increment the current streak
            else:
                max_count = max(max_count, current_count)  # Update the max streak if needed
                current_count = 0  # Reset current streak
        
        # After the loop, we need to check the last streak in case it ends with 1's
        max_count = max(max_count, current_count)
        
        return max_count
