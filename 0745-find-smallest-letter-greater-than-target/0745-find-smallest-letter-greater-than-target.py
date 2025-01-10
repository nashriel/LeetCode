class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Use binary search to find the smallest letter greater than target
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        # If no character is greater, wrap around to the first character
        return letters[left % len(letters)]
