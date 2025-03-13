# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(n):
            if n==0:  # n is as an index
               return [1]
            upper=pascal(n-1)
            next_row=[1]*(len(upper)+1)
            for i in range(1,len(upper)):
                next_row[i]=upper[i]+upper[i-1]
            return next_row
            res.append(next_row) 
        return pascal(rowIndex)
        return res





            
        