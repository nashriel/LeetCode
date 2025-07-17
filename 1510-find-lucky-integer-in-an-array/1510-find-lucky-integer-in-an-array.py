class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = [-1]
        for i in set(arr):
            if (arr.count(i) == i):
                result.append(i)
        return max(result)