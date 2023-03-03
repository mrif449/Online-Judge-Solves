def formingMagicSquare(s):
    # Define all possible magic squares
    magic_squares = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                     [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                     [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                     [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                     [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                     [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                     [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                     [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    
    # Calculate the cost of converting s to each magic square and return the minimum cost
    min_cost = float('inf')
    for square in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(square[i][j] - s[i][j])
        if cost < min_cost:
            min_cost = cost
    return min_cost

s = []
for x in range(3):
    array = list(map(int, input().split()))
    s.append(array)
print(formingMagicSquare(s))