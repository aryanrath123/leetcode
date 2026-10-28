class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])

        apply_cell = lambda previous_xors, cell_value: {
            path_xor ^ cell_value
            for path_xor in previous_xors
        }

        dp = [set() for _ in range(columns)]

        for row in range(rows):
            for column in range(columns):
                if row == 0 and column == 0:
                    dp[column] = {grid[row][column]}
                    continue

                previous_xors = set()

                if row > 0:
                    previous_xors.update(dp[column])

                if column > 0:
                    previous_xors.update(dp[column - 1])

                dp[column] = apply_cell(
                    previous_xors,
                    grid[row][column],
                )

        return min(dp[-1])