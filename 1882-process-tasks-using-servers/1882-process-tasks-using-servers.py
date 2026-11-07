import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []
        time = 0

        for i, t in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                _, w, s = heapq.heappop(busy)
                heapq.heappush(free, (w, s))

            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    _, w, s = heapq.heappop(busy)
                    heapq.heappush(free, (w, s))

            w, s = heapq.heappop(free)
            ans.append(s)
            heapq.heappush(busy, (time + t, w, s))

        return ans