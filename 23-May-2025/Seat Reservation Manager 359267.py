# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.unreserved=[i for i in range(1,n+1)]
    def reserve(self) -> int:
        return heapq.heappop(self.unreserved)
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved,seatNumber)
        
 

