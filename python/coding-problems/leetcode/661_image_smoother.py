# https://leetcode.com/problems/image-smoother/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        num_rows = len(img)
        num_cols = len(img[0])
        result = [[0 for col in range(num_cols)] for row in range(num_rows)]

        for row in range(num_rows):
            for col in range(num_cols):
                total = 0
                cell_count = 0
                start_row = max(0, row - 1)
                end_row = min(row + 1, num_rows - 1)
                start_col = max(0, col - 1)
                end_col = min(col + 1, num_cols - 1)

                for i in range(start_row, end_row + 1):
                    for j in range(start_col, end_col + 1):
                        cell_count += 1
                        total += img[i][j]
                
                result[row][col] = total // cell_count
        
        return result


