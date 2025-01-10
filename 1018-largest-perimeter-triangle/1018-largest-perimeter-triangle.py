class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the array in non-increasing order
        nums.sort(reverse=True)
        
        # Check for the largest perimeter by iterating through the sorted array
        for i in range(len(nums) - 2):
            # Check if the three sides can form a triangle
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        # If no triangle can be formed, return 0
        return 0
