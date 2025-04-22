# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen=set()
        seen.add(0)
        queue=deque()
        queue.append(0)
        while queue:
            room=queue.popleft()
            for key in rooms[room]:
                if key in seen:
                    continue
                seen.add(key)
                queue.append(key)
        return len(seen)==len(rooms)


        
        