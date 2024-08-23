A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
print("Resultant Matrix:")
print([[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A])
