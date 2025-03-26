# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = []
        for i in range(n):
            result.append('1' if nums[i][i] == '0' else '0')
        return ''.join(result)

