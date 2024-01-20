"""
    Sum of diagonal elements of spiral matrix.
"""


def spiral_matrix(n):
    """
    Create an inward spiral matrix of size n*n.
    """
    top, bottom, left, right = 0, n - 1, 0, n - 1

    count = n * n
    matrix = [[0] * n for _ in range(n)]

    while left <= right and top <= bottom:
        for pos in range(right, left - 1, -1):
            matrix[top][pos] = count
            count -= 1
        top += 1

        for pos in range(top, bottom + 1):
            matrix[pos][left] = count
            count -= 1
        left += 1

        for pos in range(left, right + 1):
            matrix[bottom][pos] = count
            count -= 1
        bottom -= 1

        for pos in range(bottom, top - 1, -1):
            matrix[pos][right] = count
            count -= 1
        right -= 1

    return matrix


def solver(n):
    """
    Find the diagonal sum of matrix of size n*n.
    """
    matrix = spiral_matrix(n)
    index = len(matrix) // 2

    diagonal_sum = matrix[index][index]

    for i in range(1, index + 1):
        diagonal_sum += (
            matrix[index + i][index + i]
            + matrix[index + i][index - i]
            + matrix[index - i][index - i]
            + matrix[index - i][index + i]
        )

    return diagonal_sum


def answer():
    """
    Find the diagonal sum of matrix of size 1001 * 1001.
    """
    return solver(1001)


if __name__ == "__main__":
    print(f"solver(5) = {solver(5)}")
    print(f"answer() = {answer()}")
