class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix_t = []
        arr = []

        for n in range(len(matrix[0])):
            for i in matrix:
                arr.append(i[n])

            matrix_t.append(arr)
            arr = []

        for row in matrix_t:
            row.reverse()

        matrix[:] = matrix_t