# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total=len(set(nums))
        distinict_number=0
        result=0
        cnt=defaultdict(int)
        right=0
        left=0
       
        for right in range(len(nums)):
            if cnt[nums[right]]==0:
                distinict_number+=1
            cnt[nums[right]]+=1
            while distinict_number==total:
                result+=len(nums)-right
                cnt[nums[left]]-=1
                if cnt[nums[left]]==0:
                    distinict_number-=1
                left+=1

        return result 




