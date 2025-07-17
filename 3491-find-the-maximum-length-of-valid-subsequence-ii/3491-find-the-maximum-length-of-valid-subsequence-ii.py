from typing import List
from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]  # dp[i][mod] = longest subsequence ending at i with mod

        res = 1  # At least 1-element sequence

        for i in range(n):
            for j in range(i):
                mod = (nums[j] + nums[i]) % k
                dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)
            for mod in dp[i]:
                res = max(res, dp[i][mod] + 1)

        return res
