class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix_t = []
        arr = []
        for n in range(len(matrix[0])):
            for i in matrix:
                arr.append(i[n])
            matrix_t.append(arr)
            arr = []
        return matrix_t

        