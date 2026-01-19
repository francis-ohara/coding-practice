"""
Problem: https://leetcode.com/problems/spiral-matrix/
"""
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        change_direction = {"right": "down", "down": "left", "left":"up", "up":"right"}
        direction = "right"
        visited_positions = set()
        position = (0, 0)

        while True:
            visited_positions.add(position)
            result.append(matrix[position[0]][position[1]])
            if direction == "right":
                next_position = (position[0], position[1] + 1)
                if next_position[1] < n_cols and next_position not in visited_positions:
                    position = next_position
                    continue
                else:
                    next_position = (position[0] + 1, position[1])
                    if next_position[0] < n_rows and next_position not in visited_positions:
                        position = next_position
                        direction = change_direction[direction]
                        continue
                    else:
                        break
            elif direction == "down":
                next_position = (position[0] + 1, position[1])
                if next_position[0] < n_rows and next_position not in visited_positions:
                    position = next_position
                    continue
                else:
                    next_position = (position[0], position[1] - 1)
                    if next_position[1] >= 0 and next_position not in visited_positions:
                        position = next_position
                        direction = change_direction[direction]
                        continue
                    else:
                        break
            elif direction == "left":
                print(position)
                next_position = (position[0], position[1] - 1)
                if next_position[1] >= 0 and next_position not in visited_positions:
                    position = next_position
                    continue
                else:
                    next_position = (position[0] - 1, position[1])
                    if next_position[0] >= 0 and next_position not in visited_positions:
                        position = next_position
                        direction = change_direction[direction]
                        continue
                    else:
                        break
            else:
                next_position = (position[0] - 1, position[1])
                if next_position[0] >= 0 and next_position not in visited_positions:
                    position = next_position
                    continue
                else:
                    next_position = (position[0], position[1] + 1)
                    if next_position[1] < n_cols and next_position not in visited_positions:
                        position = next_position
                        direction = change_direction[direction]
                        continue
                    else:
                        break
        
        return result
            


