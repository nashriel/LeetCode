from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []  # Stack to hold the current combination
        ans = []  # List to hold all valid combinations

        def backtrack(num_open, num_close):
            # Base case: if we have used all `n` open and close parentheses
            if num_open == num_close == n:
                ans.append(''.join(sol))  # Add the valid combination to ans
                return
            
            # If the number of open parentheses is less than `n`, we can add '('
            if num_open < n:
                sol.append('(')
                backtrack(num_open + 1, num_close)
                sol.pop()  # Undo the decision
            
            # If the number of close parentheses is less than open, we can add ')'
            if num_close < num_open:
                sol.append(')')
                backtrack(num_open, num_close + 1)
                sol.pop()  # Undo the decision

        # Start backtracking from zero open and close parentheses
        backtrack(0, 0)
        return ans
