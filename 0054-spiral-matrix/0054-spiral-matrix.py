class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        while matrix:
            result.extend(matrix.pop(0))
            if matrix and matrix[0]:
                for r in matrix:
                    result.append(r.pop())
            if matrix:
                result.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for r in reversed(matrix):
                    result.append(r.pop(0))
        return result

