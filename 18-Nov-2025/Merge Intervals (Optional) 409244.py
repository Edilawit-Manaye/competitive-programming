# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merge=[intervals[0]]
        for start,end in intervals:
            if start <=merge[-1][1]:
                merge[-1][1]=max(merge[-1][1],end)
            else:
                merge.append([start,end])
        return merge


        