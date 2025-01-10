from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Step 1: Get the number of rows and columns in the original matrix
        m, n = len(matrix), len(matrix[0])
        
        # Step 2: Create a new matrix of size n x m
        transposed = [[0] * m for _ in range(n)]
        
        # Step 3: Transpose the elements
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        
        return transposed
