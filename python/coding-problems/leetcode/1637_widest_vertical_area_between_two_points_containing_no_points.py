# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        x_coordinates = []
        for point in points:
            x_coordinates.append(point[0])
        x_coordinates = list(sorted(x_coordinates))

        max_difference = 0

        for i in range(len(x_coordinates) - 1):
            current_difference = x_coordinates[i + 1] - x_coordinates[i]
            if current_difference > max_difference:
                max_difference = current_difference
        return max_difference
