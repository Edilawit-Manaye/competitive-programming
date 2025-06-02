# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = 0
        count = 0
        my_dict = defaultdict(int)
        my_dict[0] = 1

        for num in nums:
            pref += num
            if pref - goal in my_dict:
                count += my_dict[pref- goal]

            my_dict[pref] += 1
            
        return count
        