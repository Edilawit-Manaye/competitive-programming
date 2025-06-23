# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row=len(mat)
        col=len(mat[0])
        diagonalDict=defaultdict(list)
        for i in range(row):
            for j in range(col):
                diagonalDict[i+j].append(mat[i][j])
        ans=[]
        for i ,val in enumerate(diagonalDict.values()):
            if i%2==0:
                ans+=val[::-1]
            else:
                ans+=val
        return ans

