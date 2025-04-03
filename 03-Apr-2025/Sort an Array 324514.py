# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            mid=len(nums)//2
            if len(nums)<=1:
                return nums
            left_arr=nums[:mid]
            right_arr=nums[mid:]
            sorted_left=mergeSort(left_arr)
            sorted_right=mergeSort(right_arr)
            return merge(sorted_left,sorted_right)
        def merge(left,right):
            i,j=0,0
            output=[]
            while i< len(left) and j<len(right):
                if left[i]<=right[j]:
                    output.append(left[i])
                    i+=1
                else:
                    output.append(right[j])
                    j+=1
            output.extend(left[i:])
            output.extend(right[j:])
            return output 
        return mergeSort(nums)
        


        