class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        from datetime import date
        a = max(date(2023, int(arriveAlice[:2]), int(arriveAlice[3:])), date(2023, int(arriveBob[:2]), int(arriveBob[3:])))
        b = min(date(2023, int(leaveAlice[:2]), int(leaveAlice[3:])), date(2023, int(leaveBob[:2]), int(leaveBob[3:])))
        return max(0, (b - a).days + 1)