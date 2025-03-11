# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums, minK, maxK):
        n = len(nums)
        count = 0
        start = 0
        min_pos = -1
        max_pos = -1

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                start = i + 1
                min_pos = max_pos = -1
            if nums[i] == minK:
                min_pos = i
            if nums[i] == maxK:
                max_pos = i

            if min_pos != -1 and max_pos != -1:
                count += min(min_pos, max_pos) - start + 1

        return count

