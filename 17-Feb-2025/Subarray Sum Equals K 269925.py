# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cumulative_sum = 0
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1  

        for num in nums:
            cumulative_sum += num
            
           
            if (cumulative_sum - k) in prefix_sum_counts:
                count += prefix_sum_counts[cumulative_sum - k]
            
            
            prefix_sum_counts[cumulative_sum] += 1

        return count