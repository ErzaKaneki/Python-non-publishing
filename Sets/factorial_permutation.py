def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

four_characters = factorial(4)
chess_pieces = factorial(6)

print(four_characters)
print(chess_pieces)