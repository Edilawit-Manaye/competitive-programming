# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def canMakeZero(k: int) -> bool:
            decrements = [0] * (len(nums) + 1)
            for i in range(k):
                l, r, val = queries[i]
                decrements[l] += val
                if r + 1 < len(nums):
                    decrements[r + 1] -= val
            current_decrement = 0
            for i in range(len(nums)):
                current_decrement += decrements[i]
                if nums[i] - current_decrement > 0:
                    return False
            return True

        left, right = 0, len(queries)
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if canMakeZero(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

