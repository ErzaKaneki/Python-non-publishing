def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

four_characters = factorial(4)
chess_pieces = factorial(6)

# print(four_characters)#Permutations
# print(chess_pieces)
# print(factorial(50))  #Permutations of a Subset
# print(factorial(50 - 7))
# print(factorial(50) / factorial(50 - 7))

def P(n, r):
    return factorial(n) / factorial(n - r) #Combination

#52 card deck, 13 card hand

unsorted_thirteen = P(52, 13)
thirteen_cards = factorial(13)
sorted_thirteen = P(52, 13) / factorial(13)

def C(n, r):
    return P(n, r) / factorial(r) #Permutations With Identical Items

#print(factorial(13))
this = factorial(13) / (factorial(2) * factorial(2) * factorial(2))
#print(this)
that = C(13, 2) * C(11, 2) * C(9, 2) * factorial(7)
#print(that)
#print(this == that) #True

# 2 buckets 3 different color of balls  #Selecting Items From a Multiset
#bucket 1 = 12 balls
bucket1 = C(12 + 3 - 1, 12)
bucket2 = C(8 + 3 - 1, 8)
#print(bucket2)
#print(3 ** 12)

#Element Composition
# print(factorial(7))
# print(factorial(7) / (factorial(2) * factorial(3)))

#Breaking a Problem Down Into Subcases
#4 english letters one C and one M, ways to place c =
# num_ways_c = C(4, 1)
# print(num_ways_c)
# num_ways_m = C(3, 1)
# print(num_ways_m)
# num_ways_remaining = 24 ** 2
# print(num_ways_remaining)
# print(num_ways_c * num_ways_m * num_ways_remaining)

chess = C(10,3) * C(8,3)
google = C(6,2) * C(4,2) * 2
marbles = C(12,5)
arr_5_marbles = P(12,5)
