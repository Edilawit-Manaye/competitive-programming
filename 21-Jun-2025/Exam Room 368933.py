# Problem: Exam Room - https://leetcode.com/problems/exam-room/description/

class ExamRoom:
    def __init__(self, n: int):
        self.num = n
        self.seats = []
        
    def seat(self) -> int:
        if not self.seats:
            seat = 0
        else:
            max_distance = 0
            seat = 0
            if self.seats[0] > 0:
                max_distance = self.seats[0]
                seat = 0
            for i in range(1, len(self.seats)):
                distance = (self.seats[i] - self.seats[i - 1]) // 2
                if distance > max_distance:
                    max_distance = distance
                    seat = self.seats[i - 1] + distance
            if self.num - 1 - self.seats[-1] > max_distance:
                seat = self.num - 1
        self.seats.append(seat)
        self.seats.sort()
        return seat

    def leave(self, p: int) -> None:
        self.seats.remove(p)