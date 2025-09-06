# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {value: index for index, value in enumerate(list1)}
        min = float('inf')
        result = []

        for index, value in enumerate(list2):
            if value in index_map:
                index_sum = index + index_map[value]
                if index_sum < min:
                    min= index_sum
                    result = [value]
                elif index_sum == min:
                    result.append(value)
        return result
        
       