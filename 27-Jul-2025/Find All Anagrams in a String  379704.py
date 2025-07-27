# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self,s:str,p:str)->list[int]:
        if len(s)< len(p):
            return []
        res=[]
        s_count=defaultdict(int)
        p_count=defaultdict(int)
        for i in range(len(p)):
            p_count[p[i]]+=1
            s_count[s[i]]+=1
        if p_count==s_count:
            res.append(0)
        l=0
        for k in range(len(p),len(s)):
            s_count[s[k]]+=1
            s_count[s[l]]-=1
            if s_count[s[l]]==0:
                 s_count.pop(s[l])
            l+=1
            if p_count==s_count:
                res.append(l)
        return res 
    