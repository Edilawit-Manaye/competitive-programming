# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        
        for numPassengers, start, end in trips:
            events.append((start, numPassengers))
            events.append((end, -numPassengers))
        
        events.sort(key=lambda x: (x[0], x[1]))
        
        current_passengers = 0
        
        for location, change in events:
            current_passengers += change
            if current_passengers > capacity:
                return False
        
        return True