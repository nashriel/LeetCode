class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {} 
        for i in range(len(nums)):
            h[nums[i]] = i
        for i in range(len(nums)):
            required = target - nums[i]
            if required in h and h[required] != i:
                return [i, h[required]]
            