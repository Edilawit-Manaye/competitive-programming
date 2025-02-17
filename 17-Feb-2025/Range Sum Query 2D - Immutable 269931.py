# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:  
    def __init__(self, matrix):  
        if not matrix or not matrix[0]:  
            self.prefix_sum = []  
            return  
        self.matrix = matrix
        self.rows = len(matrix)  
        self.cols = len(matrix[0]) 
        
        for row in range(self.rows):  
            for col in range(self.cols):
                up = self.matrix[row - 1][col] if row > 0 else 0
                left = self.matrix[row][col - 1] if col > 0 else 0
                diag = self.matrix[row - 1][col - 1] if col > 0  and row > 0 else 0
                self.matrix[row][col] += up + left - diag

    def sumRegion(self, row1, col1, row2, col2):
        res = self.matrix[row2][col2]
        up = self.matrix[row1 -1][col2] if row1 > 0 else 0
        left = self.matrix[row2][col1 - 1] if col1 > 0 else 0
        diagonal = self.matrix[row1 - 1][col1 - 1] if col1 > 0  and row1 > 0 else 0
       
        return res -up -left + diagonal

