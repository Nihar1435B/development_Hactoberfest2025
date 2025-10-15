
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1: Reverse the matrix rows (top to bottom)
        left, right = 0, len(matrix) - 1
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1

        # Step 2: Transpose the matrix
        # Swap the element at (i, j) with the element at (j, i)
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

