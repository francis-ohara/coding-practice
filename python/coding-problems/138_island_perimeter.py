# https://leetcode.com/problems/island-perimeter/?envType=problem-list-v2&envId=matrix


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    # check top
                    if row == 0:
                        perimeter += 1
                    elif grid[row - 1][col] == 0:
                        perimeter += 1

                    # check bottom
                    if row == len(grid) - 1:
                        perimeter += 1
                    elif grid[row + 1][col] == 0:
                        perimeter += 1

                    # check left
                    if col == 0:
                        perimeter += 1
                    elif grid[row][col - 1] == 0:
                        perimeter += 1

                    # check right
                    if col == len(grid[0]) - 1:
                        perimeter += 1
                    elif grid[row][col + 1] == 0:
                        perimeter += 1
        return perimeter
