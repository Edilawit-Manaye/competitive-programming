# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.small,self.large=[],[]
    def addNum(self, num: int) -> None:
        heappush(self.small,-1*num)
        if (self.small and self.large and -1 * self.small[0] >self.large[0]):
            val=-1*heappop(self.small)
            heappush(self.large,val)
        if len(self.small)>len(self.large)+1:
            val=-1*heappop(self.small)
            heappush(self.large,val)
        if len(self.large) > len(self.small)+1:
            val=heappop(self.large)
            heappush(self.small,-1*val)
    def findMedian(self) -> float:
            if len(self.small)==len(self.large) +1:
                return -1*self.small[0]
            elif len(self.large)==len(self.small)+1:
                return self.large[0]
            return (-1*self.small[0]+self.large[0])/2
            
            
            
        


