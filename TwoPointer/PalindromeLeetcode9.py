class Solution: # time=O(n) and space=O(n)
    def isPalindrome(self, x: int) -> bool:
        k=str(x)
        l,r=0,len(k)-1
        while l<=r:
            if k[l]!=k[r]:
                return False 
            l+=1
            r-=1
        return True
        
