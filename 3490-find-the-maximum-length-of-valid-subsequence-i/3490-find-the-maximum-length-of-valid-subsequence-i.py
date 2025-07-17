class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd, even = 0,0
        count = 1
        previous =nums[0] % 2
        for i in nums:
            div = i % 2
            if div:
                even+=1
            else:
                odd += 1
            if previous != div:
                count += 1
            previous = div
        return max(odd, even, count)

        