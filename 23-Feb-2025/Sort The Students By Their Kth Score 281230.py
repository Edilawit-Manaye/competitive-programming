# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # arr = []
        # for i in range(len(score)):
        #     arr.append([score[i][k],score[i]])
        # arr.sort(reverse=True)
        # ans = []
        # for i in range(len(arr)):
        #     ans.append(arr[i][1])
        # return ans
        return sorted(score,key=lambda row:row[k],reverse=True)
        

