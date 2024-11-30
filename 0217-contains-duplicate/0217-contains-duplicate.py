class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       h = set()
       for x in nums:
           if x in h:
                 return True
           else:
                h.add(x)
       return False
         