class Solution:
    def kthCharacter(self, k: int) -> str:
        count_bit = (k - 1).bit_count()
        result = chr(97 + count_bit)
        return result

