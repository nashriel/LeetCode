import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        # Left to right max-heap: minimize sum1
        left_sum = sum(nums[:n])
        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)
        left_sums = [left_sum]
        
        for i in range(n, 2*n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i] + heapq.heappop(max_heap)
            left_sums.append(left_sum)
        
        # Right to left min-heap: maximize sum2
        right_sum = sum(nums[2*n:])
        min_heap = nums[2*n:]
        heapq.heapify(min_heap)
        right_sums = [0] * (n+1)
        right_sums[n] = right_sum
        
        for i in range(2*n-1, n-1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i] - heapq.heappop(min_heap)
            right_sums[i - n] = right_sum
        
        # Find minimum difference
        result = float('inf')
        for i in range(n+1):
            result = min(result, left_sums[i] - right_sums[i])
        
        return result
