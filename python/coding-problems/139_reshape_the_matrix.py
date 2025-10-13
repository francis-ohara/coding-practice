# https://leetcode.com/problems/reshape-the-matrix/description/?envType=problem-list-v2&envId=matrix


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
            N: int = r * c
            result = [[0 for j in range(c)] for i in range(r)]

            for i in range(N):
                result[i // c][i % c] = mat[i // len(mat[0])][i % len(mat[0])]

            return result
