# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        itemm=count.items()
        sorted_count=sorted(itemm,key=lambda x: x[1],reverse=True)
        res=[]
        for num,_ in sorted_count[:k]:
            res.append(num)
        return res


        
        
       