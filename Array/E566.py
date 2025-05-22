from typing import List

[[1,2,3]
,[4,5,6]]



class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        i_r, i_c = len(mat), len(mat[0])
        if i_r * i_c != r*c : return mat
        o_mat = [[None for _ in range(c)] for _ in range(r)]
        o_r, o_c = 0, 0
        for i in range(i_r):
            for j in range(i_c):
                mat[i][j]
                o_mat[o_r][o_c] = mat[i][j]
                o_c += 1
                if o_c == c:
                    o_c = 0
                    o_r +=1
        return o_mat


# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         res = [[None for _ in range(c)] for _ in range(r)]
#         if r*c!=len(mat)*len(mat[0]):
#             return mat
#         row=col=0
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 res[row][col]= mat[i][j]
#                 col+=1
#                 if col==c:
#                     row+=1
#                     col=0
#         return res


# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         if r*c!=len(mat)*len(mat[0]):
#             return mat
#         queue = [cell for row in mat for cell in row]
#         return [[queue.pop(0) for _ in range(c)] for _ in range(r)]

