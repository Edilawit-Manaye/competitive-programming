class Solution: # time and space=O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index={}
        for i,val in enumerate(nums):
            target_half=target-val
            if target_half in val_index:
                return  [i,val_index[target_half]]
            val_index[val]=i
        return []
            
