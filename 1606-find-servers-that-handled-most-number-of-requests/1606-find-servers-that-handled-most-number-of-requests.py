class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        import heapq

        bit = [0] + [i & -i for i in range(1, k + 1)]
        busy = []
        count = [0] * k

        def update(i, v):
            i += 1
            while i <= k:
                bit[i] += v
                i += i & -i

        def prefix(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        def find(x):
            i = 0
            step = 1 << (k.bit_length() - 1)
            while step:
                j = i + step
                if j <= k and bit[j] < x:
                    i = j
                    x -= bit[j]
                step >>= 1
            return i

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                _, s = heapq.heappop(busy)
                update(s, 1)

            total = prefix(k)
            if total == 0:
                continue

            start = i % k
            before = prefix(start)
            s = find(before + 1 if total > before else 1)

            update(s, -1)
            count[s] += 1
            heapq.heappush(busy, (arrival[i] + load[i], s))

        m = max(count)
        return [i for i in range(k) if count[i] == m]