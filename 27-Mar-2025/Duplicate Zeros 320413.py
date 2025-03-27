# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr):
        zeros = 0
        n = len(arr)
        
        for num in arr:
            if num == 0:
                zeros += 1
        
        j = n + zeros - 1
        for i in range(n - 1, -1, -1):
            if j < n:
                arr[j] = arr[i]
            j -= 1
            
            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1

